radiuses =int(input("Please enter the radiuses of circle "))

cir_aria=22/7* radiuses **2
len1=int(input("Please enter the length of parallel base "))
len2=int(input("Please enter the length of 2nd parallel base "))
widt=int(input("Please enter the width between parallel bases "))
trap_aria=len1+len2/2*widt
print("Aria of trapezoid is =", trap_aria)
print("Aria of circle is =", cir_aria)
