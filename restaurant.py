'''
CS 5001
Spring 2026
Natalia Gerasimova
'''
TAX = 0.08
TIP = 0.18

def main():
    """
    This function calculates tax amount, tip amount and the total cost
    based on client's meal cost.
    """
    cost_of_dish = abs((float(input("Please, enter the meal cost: "))))
    tax_computation = cost_of_dish * TAX 
    tip_conputation = cost_of_dish * TIP
    total_meal_cost = cost_of_dish + tax_computation + tip_conputation
    print(f"Thank you for visiting us. The tax amount is ${tax_computation:.2f}, the tip amount is ${tip_conputation:.2f}.")
    print(f"Total cost is ${total_meal_cost:.2f}")

if __name__ == "__main__":
    main()