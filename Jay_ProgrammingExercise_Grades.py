import csv

"""
Name: Jay Genao
Date: February 23, 2026

Program Description:
This program asks the instructor how many students they want to enter.
It then collects each student's first name, last name, and three exam grades.
The program uses Python's csv module to write the data into a file named grades.csv.
The file includes a header row: First Name, Last Name, Exam 1, Exam 2, Exam 3.
"""


def get_student_record(student_number):
    """
    Brief Description:
        Collects one student's name and three exam grades from the user.

    Parameters:
        student_number (int): The current student number being entered (1-based).

    Variables:
        first_name (str): Student's first name.
        last_name (str): Student's last name.
        exam1 (int): Exam 1 grade.
        exam2 (int): Exam 2 grade.
        exam3 (int): Exam 3 grade.

    Logical Steps:
        1. Prompt the user for the student's first name and last name.
        2. Prompt the user for three exam grades.
        3. Convert the grades to integers.
        4. Return the completed record as a list.

    Return:
        list: A list containing [first_name, last_name, exam1, exam2, exam3].
    """
    print(f"\n--- Enter Student {student_number} ---")

    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    exam1 = int(input("Exam 1 grade: ").strip())
    exam2 = int(input("Exam 2 grade: ").strip())
    exam3 = int(input("Exam 3 grade: ").strip())

    return [first_name, last_name, exam1, exam2, exam3]


def write_grades_csv(filename, records):
    """
    Brief Description:
        Writes student grade records to a CSV file with a required header row.

    Parameters:
        filename (str): Name of the CSV file to write (ex: 'grades.csv').
        records (list): List of student records, where each record is a list.

    Variables:
        header (list[str]): Header row required by the assignment.

    Logical Steps:
        1. Create the required header list.
        2. Open the CSV file using the with keyword.
        3. Create a CSV writer object.
        4. Write the header row.
        5. Write each student record row.

    Return:
        None
    """
    header = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(records)


def main():
    """
    Brief Description:
        Main function that gathers student information and creates grades.csv.

    Parameters:
        None

    Variables:
        num_students (int): Number of students the instructor wants to enter.
        filename (str): The output CSV filename.
        records (list): List of all student records.

    Logical Steps:
        1. Ask how many students will be entered.
        2. Loop that many times and collect each student record.
        3. Write the records to grades.csv using the csv module and with keyword.
        4. Print a success message.

    Return:
        None
    """
    filename = "grades.csv"
    records = []

    num_students = int(input("How many students do you want to enter? ").strip())

    for i in range(1, num_students + 1):
        record = get_student_record(i)
        records.append(record)

    write_grades_csv(filename, records)

    print(f"\nSuccess: '{filename}' was created with {num_students} student record(s).")


if __name__ == "__main__":
    main()