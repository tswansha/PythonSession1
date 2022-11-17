'''This program objective is when user given his height and weight
calcualte BMI value and classify his status based on his BMI
classes are Underweight,Healthy,Overweight and Obses'''

#collect height from user and convert it to float and assign it to variable height
height=float(input("Please enter your height in meters"))
#collect weight from user and convert it to float and assign it to variable weight
weight=float(input("Please enter your weight in kilograms"))

#calculate BMI value
BMI=weight/(height**2)
#if BMI is less than 17.0 print you are Underweight
if (BMI<17.0):
    print("You are Underweight")
#if BMI is more than or equal 17.0 but/and less than 25.0 print you are Healthy
elif (BMI>=17.0 and BMI<25.0):
    print("You are Healthy")
#if BMI is more than or equal 25.0 but/and less than 35.0 print you are Overweight
elif (BMI>=25.0 and BMI<35.0):
    print("You are Overweight")
#otherwise you are Obses
else:
    print("You are Obses")
