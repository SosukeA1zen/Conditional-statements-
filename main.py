# no=int(input("Enter number"))
# if no>50:
#     print("Number is greater than 50")
# else:
# #     print("Number is less than 50")
# no=int(input("Enter number to check positive or negative"))
# if no>0:
#     print("Number is positive")
# else:
#     print("Number is negative")
height=float(input("Enter your height in cm"))
weight=float(input("Enter your weight in kg"))

BMI=weight/(height/100)**2
print("Your BMI is",BMI)
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=29.9:
    print("You are overweight")
elif BMI<=34.9:
    print("You are severely overweight")
elif BMI<=39.9:
    print("You are obese")
else:
    print("You are severely obese")
    