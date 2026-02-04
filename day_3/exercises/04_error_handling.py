"""
Error Handling Exercises - Day 3

Practice using try/except blocks, creating custom exceptions, and implementing
proper error handling strategies. Learn to write robust code that fails gracefully.

Your tasks:
1. Implement email validation with custom exceptions
2. Create safe file reading with try/except/else/finally
3. Build a banking transaction system with custom exceptions
4. Implement exception chaining and re-raising

Run the tests with: pytest tests/test_04_error_handling.py
"""


# Exercise 1: Email Validation with Custom Exception
# TODO: Create a custom exception for invalid emails
class InvalidEmailError:
    """
    TODO: Make this inherit from Exception
    TODO: Add proper docstring explaining when this is raised
    TODO: Add __init__ method that accepts email and reason parameters

    :param email: The invalid email address
    :type email: str
    :param reason: Reason why the email is invalid
    :type reason: str
    """

    pass


# TODO: Implement email validation function
def validate_email(email):
    """
    Validate email address format.

    TODO: Add type hints for parameter and return
    TODO: Raise InvalidEmailError if email is empty
    TODO: Raise InvalidEmailError if email doesn't contain '@'
    TODO: Raise InvalidEmailError if email doesn't contain '.'
    TODO: Return True if email is valid
    TODO: Add proper Sphinx docstring with :raises: annotation

    :param email: Email address to validate
    :type email: str
    :return: True if email is valid
    :rtype: bool
    :raises InvalidEmailError: If email format is invalid
    """
    pass


# Exercise 2: Safe File Reading
# TODO: Implement safe file reading with complete error handling
def read_json_file(filename):
    """
    Read and parse JSON file with proper error handling.

    TODO: Add type hints for parameter and return
    TODO: Use try/except/else/finally structure
    TODO: Handle FileNotFoundError - return None and print error
    TODO: Handle json.JSONDecodeError - return None and print error
    TODO: In else block: print success message with data size
    TODO: In finally block: print "File operation completed"
    TODO: Add proper Sphinx docstring

    :param filename: Path to JSON file
    :type filename: str
    :return: Parsed JSON data or None if error
    :rtype: dict | None
    """
    pass


# Exercise 3: Banking Transaction System
# TODO: Create custom exception for insufficient funds
class InsufficientFundsError:
    """
    TODO: Make this inherit from Exception
    TODO: Add docstring explaining when this is raised
    TODO: Add __init__ that accepts balance, amount, and calculates shortfall
    TODO: Store balance, amount, and shortfall as instance attributes

    :param balance: Current account balance
    :type balance: float
    :param amount: Requested withdrawal amount
    :type amount: float
    """

    pass


# TODO: Create custom exception for invalid transactions
class InvalidTransactionError:
    """
    TODO: Make this inherit from Exception
    TODO: Add docstring explaining when this is raised
    TODO: Add __init__ that accepts a message parameter

    :param message: Description of why transaction is invalid
    :type message: str
    """

    pass


# TODO: Implement money transfer function
def transfer_money(accounts, from_account, to_account, amount):
    """
    Transfer money between accounts.

    TODO: Add type hints for all parameters and return
    TODO: Validate amount > 0, raise InvalidTransactionError if not
    TODO: Check if from_account exists, raise KeyError if not
    TODO: Check if to_account exists, raise KeyError if not
    TODO: Check sufficient funds, raise InsufficientFundsError if not
    TODO: Perform the transfer (subtract from source, add to destination)
    TODO: Return True on success
    TODO: Add proper Sphinx docstring with all :raises: annotations

    :param accounts: Dictionary mapping account names to balances
    :type accounts: dict[str, float]
    :param from_account: Source account name
    :type from_account: str
    :param to_account: Destination account name
    :type to_account: str
    :param amount: Amount to transfer
    :type amount: float
    :return: True if transfer successful
    :rtype: bool
    :raises InvalidTransactionError: If amount is invalid
    :raises KeyError: If account doesn't exist
    :raises InsufficientFundsError: If insufficient funds
    """
    pass


# TODO: Implement transaction processor with error handling
def process_transaction(accounts, from_account, to_account, amount):
    """
    Process transaction with comprehensive error handling.

    TODO: Add type hints for all parameters and return
    TODO: Use try/except to catch InvalidTransactionError - print error and return False
    TODO: Catch KeyError - print "Account not found" and return False
    TODO: Catch InsufficientFundsError - print detailed error with shortfall and return False
    TODO: If successful, print success message and return True
    TODO: Add proper Sphinx docstring

    :param accounts: Dictionary mapping account names to balances
    :type accounts: dict[str, float]
    :param from_account: Source account name
    :type from_account: str
    :param to_account: Destination account name
    :type to_account: str
    :param amount: Amount to transfer
    :type amount: float
    :return: True if successful, False otherwise
    :rtype: bool
    """
    pass


# Exercise 4: Exception Chaining and Re-raising
# TODO: Create high-level exception for data processing errors
class DataProcessingError:
    """
    TODO: Make this inherit from Exception
    TODO: Add docstring for high-level data processing errors
    """

    pass


# TODO: Implement configuration parser with exception chaining
def parse_config(config_string):
    """
    Parse configuration string with exception chaining.

    TODO: Add type hints for parameter and return
    TODO: Try to parse config_string as JSON
    TODO: If json.JSONDecodeError occurs, raise DataProcessingError from it
    TODO: Use "raise DataProcessingError(...) from e" syntax
    TODO: Return parsed configuration dict
    TODO: Add proper Sphinx docstring with :raises: annotation

    :param config_string: JSON configuration string
    :type config_string: str
    :return: Parsed configuration
    :rtype: dict
    :raises DataProcessingError: If parsing fails
    """
    pass


# TODO: Implement function that re-raises exceptions after logging
def process_user_data(user_id):
    """
    Process user data with logging and re-raising.

    TODO: Add type hints for parameter and return
    TODO: Validate user_id > 0, raise ValueError if not
    TODO: Wrap validation in try/except
    TODO: In except: print log message with error details
    TODO: Re-raise the exception using bare "raise"
    TODO: Return success message if no error
    TODO: Add proper Sphinx docstring

    :param user_id: User identifier
    :type user_id: int
    :return: Success message
    :rtype: str
    :raises ValueError: If user_id is invalid
    """
    pass


# Exercise 5: Multiple Exception Handling
# TODO: Implement function that handles multiple exception types
def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with comprehensive error handling.

    TODO: Add type hints for parameters and return
    TODO: Handle ZeroDivisionError - return None and print error
    TODO: Handle TypeError - return None and print error about non-numeric values
    TODO: Return the division result if successful
    TODO: Add proper Sphinx docstring

    :param numerator: Number to divide
    :type numerator: float
    :param denominator: Number to divide by
    :type denominator: float
    :return: Division result or None if error
    :rtype: float | None
    """
    pass


# TODO: Implement function with multiple specific exception handlers
def get_user_age(users, username):
    """
    Get user age with multiple exception handling.

    TODO: Add type hints for parameters and return
    TODO: Try to access users[username]['age']
    TODO: Handle KeyError if username not found - return -1
    TODO: Handle TypeError if users is not a dict - return -1
    TODO: Return the age if successful
    TODO: Add proper Sphinx docstring

    :param users: Dictionary of user data
    :type users: dict[str, dict]
    :param username: Username to look up
    :type username: str
    :return: User age or -1 if error
    :rtype: int
    """
    pass
