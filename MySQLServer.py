import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Mankosana1969$",
            database = "my_database"
        )

        if mydb.is_connected:
            print("Database 'alx_book_store' created successfully!")
            return mydb
        
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

if __name__ == "__main__":
    conn = create_connection()
    conn.close()