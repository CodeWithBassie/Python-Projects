# BMI Calculator

#ask for user input and validate their input using try-except and while true
while True:
    try:
        weight = eval(input("Please enter your current weight in kilograms: "))
        if weight<=0: #create an if-statement should user add letters or negative numbers in place of weight
            print("Invalid input! Weight should only contain positive numeric values. Please re-enter your current weight.")
        break
    except:
        print("Error! Weight should only contain positive numeric values. Please re-enter your current weight in kilograms.")

while True:
    try:
        height = eval(input("Please enter your current height in meters: "))
        if height<=0: #create an if-statement should user add letters or negatives in place of weight
            print("Invalid input! Height should only contain positive numeric values. Please re-enter your current height.")
        break
    except:
        print("Error! Height should only contain positive numeric values. Please re-enter your current height in meters.")

#calculate the BMI using the following formula
bmi = weight/(height**2)

#group the BMI result into the following respective categories:
if bmi<18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal weight"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

#format bmi result to 1 decimal place
formatted_bmi = "{:.1f}".format(bmi)

#display BMI result and category to user
print(f"Your BMI is : {formatted_bmi}")
print(f"You currently fall under the category of: {category}")
