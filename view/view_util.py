"""
input and validation utilities
"""

def header(text):
    stars = len(text) * '*'
    print(f'\n{stars}\n{text}\n{stars}\n')
    print()


def input_positive_float(question):
    while True:
        try:
            number = float(input(question))
            if number < 0:
                print('Enter a positive number')
            else:
                return number 
        except ValueError:
            print('Enter a number.')