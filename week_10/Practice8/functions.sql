
-- PHONEBOOK — FUNCTIONS
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE (
    id          INTEGER,
    first_name  VARCHAR,
    last_name   VARCHAR,
    phone       VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        pb.id,
        pb.first_name,
        pb.last_name,
        pb.phone
    FROM phonebook pb
    WHERE
        pb.first_name ILIKE '%' || pattern || '%'
        OR pb.last_name  ILIKE '%' || pattern || '%'
        OR pb.phone      ILIKE '%' || pattern || '%'
    ORDER BY pb.last_name, pb.first_name;
END;
$$;


-- 2. Paginated contacts
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    page_number INTEGER DEFAULT 1,
    page_size   INTEGER DEFAULT 10
)
RETURNS TABLE (
    id          INTEGER,
    first_name  VARCHAR,
    last_name   VARCHAR,
    phone       VARCHAR,
    total_rows  BIGINT
)
LANGUAGE plpgsql
AS $$
DECLARE
    offset_val INTEGER;
BEGIN
    offset_val := (page_number - 1) * page_size;

    RETURN QUERY
    SELECT
        pb.id,
        pb.first_name,
        pb.last_name,
        pb.phone,
        COUNT(*) OVER () AS total_rows  
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT page_size
    OFFSET offset_val;
END;
$$;
