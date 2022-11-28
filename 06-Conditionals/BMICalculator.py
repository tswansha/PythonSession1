hight=float(input("Please enter the hight  ="))
weight=float(input("Please enter the weiht  ="))

bmi=weight/hight**2
print(bmi)
if (bmi<17):
    print("Person is underweight")
elif(bmi>=17 and bmi<25):
    print("Person have healthy weight")
elif():
    print("Person is overweight")
elif():
    print("Person is obese, Hit the gym .....")
else:
    print("input error")
