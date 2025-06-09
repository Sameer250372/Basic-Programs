def bodymassindex(weight, height):
    return round((weight/height**2),1)    
height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kilograms: "))
bmi=bodymassindex(weight, height)
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
print("Your Body Mass Index (BMI) is:", bmi)