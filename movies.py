'''
Natalia Gerasimova
CS 5001, Spring 2026
Lab 1, movies
'''
TICKET_COST = 7.95
POPCORN_COST = 8.95
DRINK_COST = 4.25
DISCOUNT = 0.10

def main():
    '''
    This function calculate the total cost before the discount 
    and the final price of the movie outing. The price is calculated based
    on the number of tickets, number of popcorns, and number of drinks, as well
    as a 10% loyalty discount.
    '''
    tickets_amount = abs(int(float(input("How many tickets do you want? "))))
    popcorn_amount = abs(int(float(input("How many buckets of popcorn? "))))
    drinks_amount = abs(int(float(input("How many drinks? "))))

    total_tickets_price = tickets_amount * TICKET_COST
    total_popcorn_price = popcorn_amount * POPCORN_COST
    total_drink_price = drinks_amount * DRINK_COST

    total_price = total_tickets_price + total_popcorn_price + total_drink_price
    total_discount = total_price * DISCOUNT
    total_price_after_discount = total_price - total_discount

    print(f"Your cost is ${total_price:.2f}")
    print(f"Your price after the discount is ${total_price_after_discount:.2f}")
           
if __name__ == "__main__":
    main()
