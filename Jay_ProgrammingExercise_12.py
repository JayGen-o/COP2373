"""
Name: Jay Genao
Date: April 13, 2026

Program Description:
This program uses NumPy to analyze student grades stored in a CSV file.
It loads the exam grades into a NumPy array, prints the first five rows,
calculates statistics for each exam, calculates overall statistics across
all exams, determines pass/fail counts for each exam, and calculates the
overall pass percentage.
"""

import csv
import numpy as np


def load_grades(filename):
    """
    Brief Description:
        Reads exam grades from a CSV file and loads them into a NumPy array.

    Parameters:
        filename (str): The name of the CSV file to read.

    Return:
        ndarray: A NumPy array containing the exam grades.
    """
    rows = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            exam1 = int(row[2])
            exam2 = int(row[3])
            exam3 = int(row[4])
            rows.append([exam1, exam2, exam3])

    return np.array(rows)


def print_first_five_rows(data):
    """
    Brief Description:
        Prints the first five rows of the dataset.

    Parameters:
        data (ndarray): NumPy array of exam grades.

    Return:
        None
    """
    print("First Five Rows of Dataset:")
    print(data[:5])


def print_exam_statistics(data):
    """
    Brief Description:
        Calculates and prints statistics for each exam column.

    Parameters:
        data (ndarray): NumPy array of exam grades.

    Return:
        None
    """
    for i in range(data.shape[1]):
        exam_scores = data[:, i]

        print(f"\nExam {i + 1} Statistics")
        print(f"Mean: {np.mean(exam_scores):.2f}")
        print(f"Median: {np.median(exam_scores):.2f}")
        print(f"Standard Deviation: {np.std(exam_scores):.2f}")
        print(f"Minimum: {np.min(exam_scores)}")
        print(f"Maximum: {np.max(exam_scores)}")


def print_overall_statistics(data):
    """
    Brief Description:
        Calculates and prints overall statistics across all exams combined.

    Parameters:
        data (ndarray): NumPy array of exam grades.

    Return:
        None
    """
    all_scores = data.flatten()

    print("\nOverall Statistics")
    print(f"Mean: {np.mean(all_scores):.2f}")
    print(f"Median: {np.median(all_scores):.2f}")
    print(f"Standard Deviation: {np.std(all_scores):.2f}")
    print(f"Minimum: {np.min(all_scores)}")
    print(f"Maximum: {np.max(all_scores)}")


def print_pass_fail_statistics(data):
    """
    Brief Description:
        Determines and prints the number of students who passed and failed each exam.

    Parameters:
        data (ndarray): NumPy array of exam grades.

    Return:
        None
    """
    for i in range(data.shape[1]):
        exam_scores = data[:, i]
        passed = np.sum(exam_scores >= 60)
        failed = np.sum(exam_scores < 60)

        print(f"\nExam {i + 1} Pass/Fail")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")


def print_overall_pass_percentage(data):
    """
    Brief Description:
        Calculates and prints the overall pass percentage across all exams.

    Parameters:
        data (ndarray): NumPy array of exam grades.

    Return:
        None
    """
    all_scores = data.flatten()
    overall_pass_percentage = (np.sum(all_scores >= 60) / all_scores.size) * 100

    print(f"\nOverall Pass Percentage: {overall_pass_percentage:.2f}%")


def main():
    """
    Brief Description:
        Loads grades from a CSV file and performs all required NumPy analysis.

    Parameters:
        None

    Return:
        None
    """
    filename = "grades.csv"
    data = load_grades(filename)

    print_first_five_rows(data)
    print_exam_statistics(data)
    print_overall_statistics(data)
    print_pass_fail_statistics(data)
    print_overall_pass_percentage(data)


if __name__ == "__main__":
    main()