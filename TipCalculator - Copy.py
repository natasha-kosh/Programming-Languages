#Natasha Wangui Ndung'u       SCT211-0057/2022

# Function to calculate the total amount to be paid per person
def calculate_total_per_person(total_bill, tip_percentage, num_people):
    tip_amount = total_bill * (tip_percentage / 100)
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / num_people
    return amount_per_person

# Prompt the user for input
total_bill = float(input("Enter the total bill amount: $"))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Check if the tip percentage is valid
if tip_percentage not in [10, 12, 15]:
    print("Invalid tip percentage. Please enter 10, 12, or 15.")
else:
    # Calculate and display the amount each person should pay
    amount_per_person = calculate_total_per_person(total_bill, tip_percentage, num_people)
    print(f"Each person should pay: ${amount_per_person:.2f}")
