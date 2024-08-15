from datetime import date


def IdValidation(user_id, input_data):
    """Check the user id is valid or not"""
    if user_id.isalnum() and user_id not in input_data:
        return True
    print("Invalid UserID or ID already exists\n")
    return False

def FirstNameValidation(first_name):
    """Check the Firstname is valid or not"""
    if first_name.isalpha():
        return True
    print("Invalid First name\n")
    return False

def LastNameValidation(last_name):
    """Check the last name is valid or not"""
    if last_name.isalpha():
        return True
    print("Invalid Last name\n")
    return False

def AgeValidation(age):
    """Chack the validation of age"""
    if age.isdigit() and 18 <= int(age) <= 100:
        return True
    print("Invalid Age\n")
    return False

def GenderValidation(gender):
    """Check gender validation"""
    if gender.lower() in ["male", "female"]:
        return True
    print("Invalid Gender\n")
    return False

def BirthDateValidation(birth_date):
    """Check the birth date validation"""
    current_year = date.today().year
    if birth_date.isdigit() and 18 <= current_year - int(birth_date) <= 120:
        return True
    print("Invalid Birth Date\n")
    return False
