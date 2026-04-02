
-- 1. UPSERT — insert or update phone if contact exists
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_first_name VARCHAR,
    p_last_name  VARCHAR,
    p_phone      VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook (first_name, last_name, phone)
    VALUES (p_first_name, p_last_name, p_phone)
    ON CONFLICT (phone) DO UPDATE
        SET first_name = EXCLUDED.first_name,
            last_name  = EXCLUDED.last_name;

    RAISE NOTICE 'Upsert done: % % → %', p_first_name, p_last_name, p_phone;
END;
$$;

-- 2. BULK INSERT — loop, validate phones, save bad ones
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_first_names  VARCHAR[],
    p_last_names   VARCHAR[],
    p_phones       VARCHAR[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i           INTEGER;
    v_phone     VARCHAR;
    v_first     VARCHAR;
    v_last      VARCHAR;
    total       INTEGER;
    inserted    INTEGER := 0;
    rejected    INTEGER := 0;
BEGIN
    total := array_length(p_first_names, 1);

    IF total IS NULL THEN
        RAISE NOTICE 'Empty input arrays.';
        RETURN;
    END IF;

    FOR i IN 1 .. total LOOP
        v_first := p_first_names[i];
        v_last  := COALESCE(p_last_names[i], '');
        v_phone := p_phones[i];

        IF v_phone ~ '^[0-9]{7,15}$' THEN
            INSERT INTO phonebook (first_name, last_name, phone)
            VALUES (v_first, v_last, v_phone)
            ON CONFLICT (phone) DO UPDATE
                SET first_name = EXCLUDED.first_name,
                    last_name  = EXCLUDED.last_name;
            inserted := inserted + 1;
        ELSE
            INSERT INTO invalid_phones (first_name, last_name, phone)
            VALUES (v_first, v_last, v_phone);
            rejected := rejected + 1;
            RAISE NOTICE 'Invalid phone skipped: % → "%"', v_first, v_phone;
        END IF;
    END LOOP;

    RAISE NOTICE 'Bulk insert complete. Inserted/Updated: %, Rejected: %', inserted, rejected;
END;
$$;


-- 3. DELETE — by first_name OR by phone
CREATE OR REPLACE PROCEDURE delete_contact(
    p_first_name VARCHAR DEFAULT NULL,
    p_phone      VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
DECLARE
    rows_deleted INTEGER;
BEGIN
    IF p_first_name IS NULL AND p_phone IS NULL THEN
        RAISE EXCEPTION 'Provide at least first_name or phone to delete.';
    END IF;

    DELETE FROM phonebook
    WHERE
        (p_first_name IS NOT NULL AND first_name ILIKE p_first_name)
        OR
        (p_phone IS NOT NULL AND phone = p_phone);

    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    RAISE NOTICE 'Deleted % row(s).', rows_deleted;
END;
$$;
