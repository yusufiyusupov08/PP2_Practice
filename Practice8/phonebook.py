from connect import get_connection

def search_contacts(pattern: str):
    conn = get_connection()
    cur  = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print(f'No contacts found for "{pattern}".')
        return []

    print(f"\n{'ID':<5} {'First':<15} {'Last':<15} {'Phone':<15}")
    print("-" * 52)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<15}")
    return rows

def upsert_contact(first_name: str, last_name: str, phone: str):
    conn = get_connection()
    conn.autocommit = True
    cur  = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s, %s);", (first_name, last_name, phone))

    cur.close()
    conn.close()
    print(f"[OK] Upsert: {first_name} {last_name} — {phone}")

def bulk_insert(users: list[dict]):
    first_names = [u.get("first", "")         for u in users]
    last_names  = [u.get("last",  "")         for u in users]
    phones      = [u.get("phone", "")         for u in users]

    conn = get_connection()
    conn.autocommit = True
    cur  = conn.cursor()

    cur.execute(
        "CALL bulk_insert_contacts(%s::varchar[], %s::varchar[], %s::varchar[]);",
        (first_names, last_names, phones)
    )

    cur.close()
    conn.close()
    print(f"[OK] Bulk insert done for {len(users)} record(s). Check invalid_phones for rejects.")

def get_contacts_paginated(page: int = 1, page_size: int = 5):
    conn = get_connection()
    cur  = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s);",
        (page, page_size)
    )
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print("No contacts on this page.")
        return []

    total = rows[0][4] if rows else 0
    print(f"\nPage {page} | Page size: {page_size} | Total rows: {total}")
    print(f"{'ID':<5} {'First':<15} {'Last':<15} {'Phone':<15}")
    print("-" * 52)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<15}")
    return rows

def delete_contact(first_name: str = None, phone: str = None):
    if not first_name and not phone:
        print("[ERROR] Provide first_name or phone.")
        return

    conn = get_connection()
    conn.autocommit = True
    cur  = conn.cursor()

    cur.execute("CALL delete_contact(%s, %s);", (first_name, phone))

    cur.close()
    conn.close()
    print(f"[OK] Delete called — name={first_name}, phone={phone}")

def show_invalid_phones():
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("SELECT id, first_name, phone, logged_at FROM invalid_phones ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("No invalid phones logged.")
        return

    print(f"\n{'ID':<5} {'Name':<15} {'Bad Phone':<20} {'Logged At'}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<20} {row[3]}")

if __name__ == "__main__":
    upsert_contact("Aziz",    "Yusupov", "998901234567")
    upsert_contact("Malika",  "Karimova","998712345678")
    upsert_contact("Jasur",   "Toshev",  "998991112233")
    upsert_contact("Aziz",    "Yusupov", "998901234567")

    bulk_insert([
        {"first": "Bobur",  "last": "Aliyev",   "phone": "998931234567"},
        {"first": "Sarvar", "last": "Nazarov",   "phone": "abc123"},
        {"first": "Nilufar","last": "Ergasheva", "phone": "99871000"},
        {"first": "Diyora", "last": "Sultanova", "phone": "998951234567"},
    ])

    search_contacts("az")
    search_contacts("9989")

    get_contacts_paginated(page=1, page_size=3)
    get_contacts_paginated(page=2, page_size=3)

    delete_contact(first_name="Jasur")
    delete_contact(phone="998951234567")

    show_invalid_phones()