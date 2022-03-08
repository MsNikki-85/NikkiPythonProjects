#BMI calculator using inches and pounds
# 🚨 Don't change the code below 👇
height = input("enter your height in inches: ")
weight = input("enter your weight in pounds: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (int(weight) / float(height) **2) * 703
bmi_as_int = int(bmi)
print(bmi_as_int)

