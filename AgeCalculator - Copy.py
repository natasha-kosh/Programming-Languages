#Natasha Wangui Ndung'u       SCT211-0057/2022


import datetime

def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    age = today - birth_date
    
    # Calculate years, months, and days
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    
    return years, months, days

while True:
    print("Options:")
    print("Enter 'calculate' to calculate age")
    print("Enter 'quit' to end the program")
    
    user_choice = input(": ")
    
    if user_choice == "quit":
        break
    
    if user_choice == "calculate":
        birth_year = int(input("Enter your birth year: "))
        birth_month = int(input("Enter your birth month: "))
        birth_day = int(input("Enter your birth day: "))
        
        years, months, days = calculate_age(birth_year, birth_month, birth_day)
        
        print(f"Your age is {years} years, {months} months, and {days} days.")
    else:
        print("Invalid input. Please enter a valid option.")
