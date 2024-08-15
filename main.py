from file_operations import load_or_create
from validation import FirstNameValidation, LastNameValidation, IdValidation, BirthDateValidation, GenderValidation, AgeValidation
from database_operations import create_database
from display_search import display, search
import os
import json
from datetime import date
import mysql.connector
from mysql.connector import Error


def main_menu():
    """List all options for the user"""
    print("\nMain Menu")
    print("1. Add New User Data")
    print("2. Display All Saved Data")
    print("3. Search for User Data")
    print("4. Exit")
    choice = input("Choose an option: ")
    return choice

def main():
    file_name = "users_data.txt"
    json_file = "users_data.json"
    input_data = load_or_create(file_name)
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            
            user_id = input("Enter your ID: ")
            if not IdValidation(user_id, input_data):
                continue
                
            first_name = input("Enter your First name: ")
            if not FirstNameValidation(first_name):
                continue

            last_name = input("Enter your Last name: ")
            if not LastNameValidation(last_name):
                continue

            age = input("Enter your age: ")
            if not AgeValidation(age):
                continue

            gender = input("Enter your gender (male/female): ")
            if not GenderValidation(gender):
                continue

            birth_date = input("Enter your Birth Year (YYYY): ")
            if not BirthDateValidation(birth_date):
                continue

            # Update the input_data dictionary with the new user information
            input_data[user_id] = {
                "user_id": user_id,
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "gender": gender,
                "birth_date": birth_date
            }

            # Write the updated input_data back to the files
            try:
                with open(file_name, "w") as file:
                    json.dump(input_data, file, indent=4)
                with open(json_file, "w") as jsonfile:
                    json.dump(input_data, jsonfile, indent=4)
                print("User data saved successfully.")
            except Exception as e:
                print(f"Error writing to file: {e}")
    
        elif choice == "2":
            try:
                display(input_data)
            except Exception as e:
                print(f"An error occurred while displaying data: {e}")

        elif choice == "3":
            while True:
                search_id = input("\nEnter the ID of the user to search or type 'no' to return to the main menu: ")
                if search_id.lower() == "no":
                    break
                try:
                    search(search_id, input_data)
                except Exception as e:
                    print(f"An error occurred while searching: {e}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

    create_database(user_id, first_name,last_name, age,gender,birth_date)

if __name__ == "__main__":
    main()