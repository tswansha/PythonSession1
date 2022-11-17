input=int(input("Please enter the number between 0-100  ="))
if input<=1000:
   if input%2==0:
       print("Number you entered is even number")
       if input<=100:
           print("Number you have entered number less than or equal to 100")
           if input<=10:
              print("Number you have entered number less than or equal to 10")
   else:
       print("Number you entered is odd number")
       if input<=100:
          print("Number you have entered number less than or equal to 100")
          if input<=10:
             print("Number you have entered number less than or equal to 10")
else:
    print("Will you ever read the advise in the messages ")
