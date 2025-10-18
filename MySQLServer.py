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

        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            return mydb

    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()