#Natasha Wangui Ndung'u      SCT211-0057/2022

# Function to calculate BMI and provide feedback
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    else:
        return "Overweight"

# Prompt the user for input
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI and provide feedback
result = calculate_bmi(weight_kg, height_m)
print(f"Your BMI is {result}.")
