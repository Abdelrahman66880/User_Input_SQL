# User_Input_Sql

## Overview

The **User Data Management System** is a Python-based application that allows users to add, display, and search for user data. This system stores user data in a text file, a JSON file, and an SQL Server database.

## Features

- **Add New User Data**: Users can input personal information, including ID, first name, last name, age, gender, and birth date.
- **Display All Saved Data**: View all user data that has been saved.
- **Search for User Data**: Find specific user data by ID.
- **Data Validation**: Validates user input to ensure it meets specified criteria (e.g., valid ID, age).
- **Data Storage**: Saves user data in a text file, a JSON file, and an SQL Server database.

## How to Use

1. **Run the main file**: Start the application by running the `main.py` file.
2. **Choose an option from the main menu**:
   - **Add New User Data** (Option 1): Allows you to input new user data.
   - **Display All Saved Data** (Option 2): Shows all data saved in the system.
   - **Search for User Data** (Option 3): Lets you search for user data by ID.
   - **Exit the System** (Option 4): Closes the application.
3. Follow the prompts to add new user data or search for existing data.

## Requirements

- Python 3.x
- `mysql` library (for SQL Server database connectivity)
- `json` library (for JSON file operations)

## Files

- `main.py`: The main program file that contains the user interface and data management logic.
- `file_operations.py`: A module that contains functions for loading and saving data to files.
- `validation.py`: A module that contains functions for validating user input data.
- `database_operations.py`: A module that contains functions for creating and interacting with the SQL Server database.
- `display_search.py`: A module that contains functions for displaying and searching user data.
- `users_data.txt`: A text file that stores user data.
- `users_data.json`: A JSON file that stores user data.

## Database Setup

Ensure that the SQL Server instance is running and that you have the appropriate permissions to create databases and tables. Adjust the connection string in `database_operations.py` if needed.
