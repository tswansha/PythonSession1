print("This program will help to find perticular number you have enterd")
print("is a prime number or not make sure you enter non negative numbers ")
number=int(input("Please input the number you wish to check ="))
counter=2
flag=0
if number<2:
    flag=1
else:
    while counter<number:
        if number%counter==0:
            flag=1
            break
        else:
            counter+=1
            continue
if flag==1:
    print("{} is non prime number ".format(number))
else:
    print("{} is prime number ".format(number))
