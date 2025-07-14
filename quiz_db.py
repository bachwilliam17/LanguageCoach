import sqlite3

def generate_quiz(database) :
    conn = sqlite3.connect(database)
    table_name = database.replace(".db", "")
    
    SQL_request = f"SELECT * from {table_name} LIMIT 6"
    current_line = conn.execute(SQL_request).fetchall()
    print(current_line)

