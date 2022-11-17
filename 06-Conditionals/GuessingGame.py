import random
randomNumber=random.randint(0,9)
print("Can you guess the number I am  thinking....?")
input=int(input("it is between 0 and 9      ="))
if input< randomNumber:
   print("Nope, My number is higer than you think")
elif input> randomNumber:
   print("Nope, My number is lower than you think")
elif input== randomNumber:
   print("Brovo , That is the exact number I am thinking ")
else:
   print("Something wrong here  ")
