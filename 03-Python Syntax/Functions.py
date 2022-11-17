#Method CalculateAria reciving rad as input parameter
def CalculateAria(rad):
#indented codes belong to CalculateAria function
   aria=22/7*rad**2
   return aria

radius =float(input("Please enter the radius of circle"))
#call the function for get output
print("Aria of circle is", CalculateAria(radius ))

rad =float(input("Please enter the radius of new circle"))
print("Aria of circle is", CalculateAria(rad))
