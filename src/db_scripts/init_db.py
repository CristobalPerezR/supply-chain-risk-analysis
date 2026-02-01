import sqlite3
import os

def _delete(deleter_path:str, conn:sqlite3.Connection) -> int: # NO NECESARIO
    with open(deleter_path) as f:
        deleter = f.read()
    conn.executescript(deleter)
    conn.commit()
    print(f"Database cleaned")
    return 0

def init_db(db_name:str):
    db_dir = os.path.join("data", "database")
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, f"{db_name}.db")
    schema_path = os.path.join("sql", "schema.sql")
    deleter_path = os.path.join("sql", "delete_db.sql")
    
    conn = None

    try:
        conn = sqlite3.connect(db_path)
        _delete(deleter_path, conn)
        with open(schema_path) as f:
            schema = f.read()
        conn.executescript(schema)
        conn.commit()
        print(f"Database initialized at {db_path}")
    except Exception as e:
        raise RuntimeError(f"Database initialization error: {e}")
    finally:
        if conn:
            conn.close()