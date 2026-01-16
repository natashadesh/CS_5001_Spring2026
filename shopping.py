'''
Natalia Gerasimova
CS 5001, Spring 2026
Homework 1, Program 1 -- AmaGone.com Shopping

It is Online Shopping Program
to calculate client's shopping bag Total Cost
and 2-Pay Plan cost. 
'''
INTEREST_RATE = 1.05
PAYNMENTS_NUMBER = 2
def main(): 
    print("Welcome to my Online Shopping Program!")
    input_product_name = input("Enter the product name: ")
    input_product_price = input(f"What is the price of {input_product_name}? ")
    input_product_quantity = input(f"How many {input_product_name}s are you purchasing? ")
    input_product_price = abs(float(input_product_price))
    input_product_quantity = abs(int(float(input_product_quantity)))
    print(f"You are buying {input_product_quantity} {input_product_name} at ${input_product_price:.2f} each.")
    total_cost = input_product_price * input_product_quantity
    print(f"Total Cost for this shopping session is ${total_cost:.2f}")
    two_pay_plan_cost = round((total_cost * INTEREST_RATE) / PAYNMENTS_NUMBER, 2)
    print(f"Our 2-Pay Plan is two equal payments of ${two_pay_plan_cost:.2f}")
    
if __name__ == "__main__":
    main()