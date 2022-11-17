inputValue=int(input("Please input greater than 0 integer and we will give you factorial ="))

if inputValue<0:
    raise ValueError("Number should be greater than 0 integer")

factorial=1
counter=1

while counter<=inputValue:
   factorial=factorial*counter
   counter=counter+1

print("Factorial of is =",factorial)
