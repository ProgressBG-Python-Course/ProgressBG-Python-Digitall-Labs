# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:

Define a function named `get_numeric_input()` that:

1. Prompts the user to enter a valid number.
2. Continuously prompts until a valid number (integer or floating-point) is entered.
3. Returns the valid number as a `float`.

The function must handle potential errors, such as:

- KeyboardInterrupt - gracefully exit, if user press 'Ctrl+C'
- Empty input - pressing Enter without typing anything.
- Invalid input - non-numeric characters.
- Any other unexpected errors that might occur during input.

"""

### Your code here
def get_numeric_input():
    """Prompts the user for a valid number and returns it as a float, handling potential errors."""

    while True:
        try:
            user_input = input("Please enter a number: ")
            if not user_input:
                raise ValueError("Input cannot be empty.")
            number = float(user_input)
            return number
        except KeyboardInterrupt:
            raise  # Re-raise KeyboardInterrupt to allow graceful exit
        except ValueError as e:
            print(f"Invalid input: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

# Example usage:
# try:
#     valid_number = get_numeric_input()
#     print("You entered:", valid_number)
# except KeyboardInterrupt:
#     print("\nProgram exited by user.")


### EXPECTED OUTPUT:

# Please enter a number: 23
# You entered: 23.0

# Please enter a number:
# Invalid input: Input cannot be empty.

# Please enter a number: o
# Invalid input: could not convert string to float: 'o'

# Please enter a number: ^C
# Program exited by user.


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:

Write a program that prompts the user to enter their name. Ensure the entered name:

1. Contains only letters.
    - tip: you can use the string.isalpha() method
2. Starts with an uppercase letter.
    - tip: you can use the string.isupper() method
3. Is at least 2 characters long.

The function must raise InvalidUserName exception if user name is not valid.

"""

### Your code here
class InvalidUserName(Exception):
    """General exception for invalid user name input."""
    pass

def get_valid_username():
    """Prompts the user for a valid username, handling potential errors."""
    while True:
        try:
            name = input("Please enter your name: ")

            if not name.isalpha():
                raise InvalidUserName("Name must contain only letters.")
            if not name[0].isupper():
                raise InvalidUserName("Name must start with an uppercase letter.")
            if len(name) < 2:
                raise InvalidUserName("Name must be at least 2 characters long.")

            return name  # Return the valid username

        except InvalidUserName as e:
            print(f"Error: {e}")


# Example usage:
# try:
#     username = get_valid_username()
#     print(f"Hello, {username}!")
# except KeyboardInterrupt:
#     print("\nProgram exited by user.")

# EXPECTED OUTPUT:
# Please enter your name: ada123
# Error: Name must contain only letters.
# Please enter your name: ada
# Error: Name must start with an uppercase letter.
# Please enter your name: A
# Error: Name must be at least 2 characters long.
# Please enter your name: Ada
# Hello, Ada!
