import random
randomNumber=random.randint(0,9)
number=int(input("please enter you guess between 0 and 9"))
if(randomNumber>number):
    print("Random number is Higher than your guess")
elif(randomNumber<number):
    print("Random number is lower than your guess")
elif(randomNumber==number):
    print("Bravo you have guess the random number ....!!!")
else:
    print("somthing is wrong here ")
print(randomNumber)
