"""
Technical Design Document: Jay_ProgrammingExercise_6
Name: Jay Genao
Date: March 2, 2026
Program Description:
This program validates a phone number, Social Security number (SSN), and ZIP code using
regular expressions. The user enters values in the main function, and the program displays
whether each value is valid. The program also includes a test function that runs multiple
valid and invalid examples to confirm the regular expressions work correctly.
"""

import re


def validate_phone(phone: str) -> bool:
    """
    Validates a U.S. phone number using regular expressions.

    Parameters:
        phone (str): The phone number entered by the user.

    Variables:
        pattern (str): Regex pattern for accepted phone formats.

    Logic:
        1. Strip leading/trailing spaces.
        2. Use regex full match to validate one of these formats:
           - 123-456-7890
           - (123) 456-7890
           - 1234567890

    Return:
        bool: True if valid, False otherwise.
    """
    phone = phone.strip()
    pattern = r"^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$"
    return re.fullmatch(pattern, phone) is not None


def validate_ssn(ssn: str) -> bool:
    """
    Validates a Social Security Number (SSN) using regular expressions.

    Parameters:
        ssn (str): The SSN entered by the user.

    Variables:
        pattern (str): Regex pattern for SSN format ###-##-####

    Logic:
        1. Strip leading/trailing spaces.
        2. Use regex full match to ensure SSN matches ###-##-####.

    Return:
        bool: True if valid, False otherwise.
    """
    ssn = ssn.strip()
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return re.fullmatch(pattern, ssn) is not None


def validate_zip(zip_code: str) -> bool:
    """
    Validates a U.S. ZIP code using regular expressions.

    Parameters:
        zip_code (str): The ZIP code entered by the user.

    Variables:
        pattern (str): Regex pattern for ZIP formats:
                       - 12345
                       - 12345-6789

    Logic:
        1. Strip leading/trailing spaces.
        2. Use regex full match to validate either 5-digit ZIP or ZIP+4.

    Return:
        bool: True if valid, False otherwise.
    """
    zip_code = zip_code.strip()
    pattern = r"^\d{5}(-\d{4})?$"
    return re.fullmatch(pattern, zip_code) is not None


def run_tests() -> None:
    """
    Runs multiple valid and invalid test cases to confirm regex correctness.

    Parameters:
        None

    Variables:
        phone_tests (list): Phone test inputs
        ssn_tests (list): SSN test inputs
        zip_tests (list): ZIP test inputs

    Logic:
        1. Print a test header for each category.
        2. Run each value through its validator.
        3. Print PASS if the result matches expected, else FAIL.

    Return:
        None
    """
    phone_tests = [
        ("123-456-7890", True),
        ("(123) 456-7890", True),
        ("1234567890", True),
        ("123.456.7890", False),
        ("(123)-456-7890", False),
        ("12-3456-7890", False),
    ]

    ssn_tests = [
        ("123-45-6789", True),
        ("123456789", False),
        ("12-345-6789", False),
        ("abc-de-ghij", False),
    ]

    zip_tests = [
        ("12345", True),
        ("12345-6789", True),
        ("1234", False),
        ("123456", False),
        ("12345-678", False),
    ]

    print("\n--- TEST RESULTS ---")

    print("\nPhone Tests:")
    for value, expected in phone_tests:
        result = validate_phone(value)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | {value} -> {result} (expected {expected})")

    print("\nSSN Tests:")
    for value, expected in ssn_tests:
        result = validate_ssn(value)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | {value} -> {result} (expected {expected})")

    print("\nZIP Tests:")
    for value, expected in zip_tests:
        result = validate_zip(value)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | {value} -> {result} (expected {expected})")


def main() -> None:
    """
    Program entry point. Collects user input and displays validation results.

    Parameters:
        None

    Variables:
        phone (str): User-entered phone number
        ssn (str): User-entered SSN
        zip_code (str): User-entered ZIP code
        phone_ok (bool): Phone validation result
        ssn_ok (bool): SSN validation result
        zip_ok (bool): ZIP validation result

    Logic:
        1. Ask the user for phone, SSN, and ZIP.
        2. Validate each input using the validator functions.
        3. Display valid/invalid results clearly.
        4. Run automated tests to show correctness.

    Return:
        None
    """
    print("Enter values to validate.\n")

    phone = input("Phone (123-456-7890 OR (123) 456-7890 OR 1234567890): ")
    ssn = input("SSN (###-##-####): ")
    zip_code = input("ZIP (##### OR #####-####): ")

    phone_ok = validate_phone(phone)
    ssn_ok = validate_ssn(ssn)
    zip_ok = validate_zip(zip_code)

    print("\n--- Validation Results ---")
    print(f"Phone: {'Valid' if phone_ok else 'Invalid'}")
    print(f"SSN:   {'Valid' if ssn_ok else 'Invalid'}")
    print(f"ZIP:   {'Valid' if zip_ok else 'Invalid'}")

    # Required testing section
    run_tests()


if __name__ == "__main__":
    main()