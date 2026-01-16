"""
Natalia Gerasimova
CS 5001, Spring 2026
On lecture coding

Age minder application
"""
DECADE = 10
def main():
    user_name = input("What is your name? ")
    user_age = abs(int(float(input("What is your age? "))))
    next_year_user_age = user_age + 1
    user_decades = user_age // DECADE
    print(f"Your name is {user_name}, your age is {user_age}. Next year you will be {next_year_user_age}.")
    print(f"Your are in {user_decades} decade.")

if __name__ == "__main__":
    main()