upper=int(input("Please Enter the upper limit ="))
counter=sum=0
while counter<=upper:
    counter+=1
    if counter%2==1:
        continue
    sum+=counter
print("Sum of even numbers from 0 to {0} = {1}". format(upper,sum))
