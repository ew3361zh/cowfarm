"""input and validation utilities for the view module"""

def header(text):
    """style function to make command-line app more engaging and distinct"""
    stars = len(text) * '*'
    print(f'\n{stars}\n{text}\n{stars}\n')
    print()


def input_positive_float(question) -> float:
    """input validation for positive float"""
    while True:
        try:
            number = float(input(question))
            if number <= 0:
                print('Enter a positive number')
            else:
                return number 
        except ValueError:
            print('Enter a number.')


def calculate_annual_cost(number_of_cows, amount_of_feed_per_cow, feed_cost_per_pound) -> float:
    """calculate cost of feed consumed for 1 pen over 1 year"""
    return number_of_cows * amount_of_feed_per_cow * feed_cost_per_pound * 365


def calculate_annual_ghg(q1, q2, q3, q4) -> float:
    """
    calculate milk yield CO2 generation based off:
    - 1 liter of milk produces 1.39 kg of CO2 equivalents to the atmosphere.
    (https://blogs.nicholas.duke.edu/citizenscientist/how-green-is-your-milk/)
    - conversion: 1 liter = 0.264172 gallons
    """
    return (q1 + q2 + q3 + q4) * 1/0.264172 * 1.39

