import csv

"""
Name: Jay Genao
Date: February 23, 2026

Program Description:
This program reads student grade data from grades.csv and displays it in a clean
tabular format. It uses the csv module and the with keyword to safely open and
read the file. The output includes the header row and each student's record.
"""


def read_grades_csv(filename):
    """
    Brief Description:
        Reads all rows from a CSV file and returns them as a list.

    Parameters:
        filename (str): Name of the CSV file to read.

    Variables:
        rows (list): Stores each row from the CSV file.

    Logical Steps:
        1. Open the CSV file using the with keyword.
        2. Use csv.reader to read each row.
        3. Store all rows in a list.
        4. Return the list.

    Return:
        list: A list of rows from the CSV file.
    """
    rows = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    return rows


def display_table(rows):
    """
    Brief Description:
        Displays CSV rows in a simple tabular format with aligned columns.

    Parameters:
        rows (list): A list of rows (each row is a list of values).

    Variables:
        col_widths (list[int]): Tracks the max width of each column for formatting.
        row (list): One row of data from the CSV.

    Logical Steps:
        1. Find the max width for each column.
        2. Print each row with padding so columns line up.
        3. Print a divider line after the header.

    Return:
        None
    """
    if not rows:
        print("No data found.")
        return

    # Determine column widths
    col_count = len(rows[0])
    col_widths = [0] * col_count

    for row in rows:
        for i in range(col_count):
            col_widths[i] = max(col_widths[i], len(str(row[i])))

    # Print rows with alignment
    for index, row in enumerate(rows):
        line = ""
        for i in range(col_count):
            line += str(row[i]).ljust(col_widths[i] + 3)
        print(line)

        # Divider after header row
        if index == 0:
            divider = ""
            for w in col_widths:
                divider += ("-" * w).ljust(w + 3)
            print(divider)


def main():
    """
    Brief Description:
        Loads grades.csv and prints it as a formatted table.

    Parameters:
        None

    Variables:
        filename (str): CSV filename to read.
        rows (list): Rows read from the CSV.

    Logical Steps:
        1. Read the CSV file into rows.
        2. Display the rows in a table format.

    Return:
        None
    """
    filename = "grades.csv"
    rows = read_grades_csv(filename)
    print("\n--- Grades Table ---\n")
    display_table(rows)


if __name__ == "__main__":
    main()