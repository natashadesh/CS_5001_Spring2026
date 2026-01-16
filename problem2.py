'''
Natalia Gerasimova
CS 5001, Spring 2026
Lab 1, problem_2
'''
CAR_INSURANCE_PER_YEAR = 1600
MILES_RATE = 0.005
def main():
    '''
    This function calculates the monthly costs of owning a car
    based on the cost of car insurance, monthly maintenance and fuel costs.
    '''
    miles_per_month = abs(int(input("How many miles per month do you drive?  ")))
    gallon_price = abs(float(input("What is the average price of a gallon of gas?  ")))
    miles_per_gallon = abs(float(input("How many miles per gallon does your car get on average? ")))

    maintenance = miles_per_month * MILES_RATE
    fuel_cost = (miles_per_month / miles_per_gallon) * gallon_price
    total_expense_per_month = CAR_INSURANCE_PER_YEAR / 12 + maintenance + fuel_cost

    print(f"Your total expense per month is is ${total_expense_per_month:.2f}")
if __name__ == "__main__":
    main()