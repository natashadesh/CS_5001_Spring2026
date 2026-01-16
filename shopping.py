'''
Natalia Gerasimova
CS 5001, Spring 2026
Homework 1, Program 1 -- AmaGone.com Shopping
'''
INTEREST_RATE = 1.05
PAYNMENTS_NUMBER = 2
def main(): 
    '''
    This function calculates client's shopping bag Total Cost
    and 2-Pay Plan cost based on product name, price and quantity.   
    '''
    print("Welcome to my Online Shopping Program!")
    item_name = input("Enter the product name: ")
    item_price = input(f"What is the price of {item_name}? ")
    item_amount = input(
        f"How many {item_name}s are you purchasing? "
    )
    item_price = abs(float(item_price))
    item_amount = abs(int(float(item_amount)))
    print(
        f"You are buying {item_amount} {item_name} at ${item_price:.2f} each."
    )
    total_cost = item_price * item_amount
    print(f"Total Cost for this shopping session is ${total_cost:.2f}")
    two_pay_plan = round((total_cost * INTEREST_RATE) / PAYNMENTS_NUMBER, 2)
    print(f"Our 2-Pay Plan is two equal payments of ${two_pay_plan:.2f}")
    
if __name__ == "__main__":
    main()