"""
Name: Jay Genao
Date: April 20, 2026

Program Description:
This program creates a SQLite database named population_JG.db and a table named
population. It inserts 2023 population data for 10 Florida cities, simulates
population growth or decline for the next 20 years, stores that data in the table,
and uses matplotlib to display population growth for a city chosen by the user.
"""

import random
import sqlite3
import matplotlib.pyplot as plt


def create_database():
    """
    Creates the database and population table, then inserts the 2023 starting data
    for 10 Florida cities.

    Parameters:
        None

    Variables:
        conn (sqlite3.Connection): Connection to the SQLite database.
        cursor (sqlite3.Cursor): Cursor used to execute SQL commands.
        starting_data (list[tuple]): Starting city, year, and population records.

    Logical Steps:
        1. Connect to the database named population_JG.db.
        2. Drop the population table if it already exists.
        3. Create a new population table with city, year, and population fields.
        4. Insert the 2023 population data for 10 Florida cities.
        5. Commit the changes and close the connection.

    Return:
        None
    """
    conn = sqlite3.connect("population_JG.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS population")

    cursor.execute("""
        CREATE TABLE population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # Example 2023 starter data for 10 Florida cities
    starting_data = [
        ("Jacksonville", 2023, 985843),
        ("Miami", 2023, 467963),
        ("Tampa", 2023, 403364),
        ("Orlando", 2023, 320742),
        ("St. Petersburg", 2023, 263553),
        ("Hialeah", 2023, 225999),
        ("Port St. Lucie", 2023, 236169),
        ("Cape Coral", 2023, 230326),
        ("Tallahassee", 2023, 204627),
        ("Fort Lauderdale", 2023, 186208)
    ]

    cursor.executemany(
        "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
        starting_data
    )

    conn.commit()
    conn.close()


def simulate_population_growth():
    """
    Simulates 20 years of population growth or decline and inserts the results into
    the population table.

    Parameters:
        None

    Variables:
        conn (sqlite3.Connection): Connection to the SQLite database.
        cursor (sqlite3.Cursor): Cursor used to execute SQL commands.
        cities (list[tuple]): List of city names and 2023 populations.
        city (str): Current city being processed.
        start_population (int): Starting population for 2023.
        current_population (int): Updated population each year.
        year (int): Current simulated year.
        rate (float): Annual growth or decline rate.

    Logical Steps:
        1. Connect to the database.
        2. Read all 2023 city population records.
        3. For each city, simulate the next 20 years.
        4. Use a random rate each year between -1.5% and 3.0%.
        5. Calculate the new population and insert it into the table.
        6. Commit the changes and close the connection.

    Return:
        None
    """
    conn = sqlite3.connect("population_JG.db")
    cursor = conn.cursor()

    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    cities = cursor.fetchall()

    random.seed(2373)

    for city, start_population in cities:
        current_population = start_population

        for year in range(2024, 2044):
            rate = random.uniform(-0.015, 0.03)
            current_population = int(current_population * (1 + rate))

            cursor.execute(
                "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                (city, year, current_population)
            )

    conn.commit()
    conn.close()


def plot_population_growth():
    """
    Displays a population growth chart for the city chosen by the user.

    Parameters:
        None

    Variables:
        conn (sqlite3.Connection): Connection to the SQLite database.
        cursor (sqlite3.Cursor): Cursor used to execute SQL commands.
        cities (list[str]): List of available city names.
        choice (str): City chosen by the user.
        rows (list[tuple]): Year and population rows for the chosen city.
        years (list[int]): Years for the chart.
        populations (list[int]): Population values for the chart.

    Logical Steps:
        1. Connect to the database.
        2. Get the list of distinct city names.
        3. Display the city options to the user.
        4. Ask the user to choose one city.
        5. Read all year and population values for that city.
        6. Plot the data with matplotlib.
        7. Close the database connection.

    Return:
        None
    """
    conn = sqlite3.connect("population_JG.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT city FROM population ORDER BY city")
    cities = [row[0] for row in cursor.fetchall()]

    print("\nChoose a city to display:")
    for index, city in enumerate(cities, start=1):
        print(f"{index}. {city}")

    choice_number = int(input("\nEnter the number of the city: ").strip())

    if choice_number < 1 or choice_number > len(cities):
        print("Invalid choice.")
        conn.close()
        return

    choice = cities[choice_number - 1]

    cursor.execute(
        "SELECT year, population FROM population WHERE city = ? ORDER BY year",
        (choice,)
    )
    rows = cursor.fetchall()

    years = [row[0] for row in rows]
    populations = [row[1] for row in rows]

    print(f"\nDisplaying population growth for {choice}...")

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker="o")
    plt.title(f"Population Growth for {choice}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    conn.close()


def main():
    """
    Runs the full program.

    Parameters:
        None

    Variables:
        None

    Logical Steps:
        1. Create the database and table.
        2. Insert the 2023 city population data.
        3. Simulate 20 years of growth or decline.
        4. Let the user choose a city.
        5. Display the population growth chart for that city.

    Return:
        None
    """
    create_database()
    simulate_population_growth()
    plot_population_growth()


if __name__ == "__main__":
    main()