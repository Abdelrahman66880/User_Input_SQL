def display(data_dict):
    """Display the saved data"""
    if not data_dict:
        print("No data to display")
    else:
        for user_id, user_data in data_dict.items():
            print(f"\nUser ID: {user_data['user_id']}")
            print(f"First Name: {user_data['first_name']}")
            print(f"Last Name: {user_data['last_name']}")
            print(f"Age: {user_data['age']}")
            print(f"Gender: {user_data['gender']}")
            print(f"Birth Year: {user_data['birth_date']}")

def search(user_id, data_dict):
    """Search for certain user"""
    if not data_dict:
        print("No data to search")
    elif user_id in data_dict:
        user_data = data_dict[user_id]
        print(f"\nUser ID: {user_data['user_id']}")
        print(f"First Name: {user_data['first_name']}")
        print(f"Last Name: {user_data['last_name']}")
        print(f"Age: {user_data['age']}")
        print(f"Gender: {user_data['gender']}")
        print(f"Birth Year: {user_data['birth_date']}")
    else:
        print("User ID not found")
