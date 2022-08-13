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
            if number <= 0:
                print('Enter a positive number')
            else:
                return number 
        except ValueError:
            print('Enter a number.')

def calculate_annual_cost(number_of_cows, amount_of_feed_per_cow, feed_cost_per_pound):
    return number_of_cows * amount_of_feed_per_cow * feed_cost_per_pound * 365

"""
Estimates from online searches: 
1 dairy cow produces avg of 7.5 gallons milk/day 
https://www.ciwf.com/farmed-animals/cows/dairy-cows/#:~:text=Milk%20production%20per%20cow%20has,gallon%20of%20milk%20per%20day
1 liter of milk produces 1.39 kg of CO2 equivalents to the atmosphere
https://blogs.nicholas.duke.edu/citizenscientist/how-green-is-your-milk/
1 liter = 0.264172 gallons
7.5 gallons of milk produces ~2.7539931 kg of CO2 per day
"""

def calculate_annual_ghg(q1, q2, q3, q4):
    return (q1 + q2 + q3 + q4) * 0.264172 * 1.39

