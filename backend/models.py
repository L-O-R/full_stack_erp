import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = "nexgen_erg.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # User model
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        is_superuser BOOLEAN NOT NULL DEFAULT 0
                   )
                   
                   ''')
    
    conn.commit()
    conn.close()


def create_user(username , password , is_superuser= False):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    hashed_pw = generate_password_hash(password)
    try:
        cursor.execute('INSERT INTO users (username, password, is_superuser) VALUES (?, ?, ?)', (username, hashed_pw, 1 if is_superuser else 0))
        conn.commit()
    except sqlite3.IntegrityError:
        print("USer Already Exits!")
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    create_user("John", "admin123", is_superuser=True)
    print("databse intialized and user created")