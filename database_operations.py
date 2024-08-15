import mysql.connector
from mysql.connector import Error


def create_database(user_id, first_name, last_name, age, gender, birth_date):
    """Check the connection and create database if not exists"""
    try:
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="55555",
            database="UserDatabase"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS UserDatabase")
            cursor.execute("USE UserDatabase")

            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id VARCHAR(255) PRIMARY KEY,
                    first_name VARCHAR(255),
                    last_name VARCHAR(255),
                    age INT,
                    gender VARCHAR(50),
                    birth_date YEAR
                )
            """)

            # Insert user data into the table
            query = """INSERT INTO users (user_id, first_name, last_name, age, gender, birth_date)
                        VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (user_id, first_name, last_name, int(age), gender, birth_date))
            connection.commit()

            print("User data inserted successfully into the database.")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
