import mysql.connector
from mysql.connector import Error

def create_database():
    """Create alx_book_store database if it doesn't exist"""
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:  # Fixed this line
        print(f"Error: {e}")
        print("Failed to connect to the database")
        
    finally:
        # Close connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Execute the function when script runs
if __name__ == "__main__":
    create_database()