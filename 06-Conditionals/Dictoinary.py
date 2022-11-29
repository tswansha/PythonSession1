import json

data = json.load(open("data.json"))
word = input("Please Enter the word you need to seacrh on the dictionary  =")
word = word.lower()
if word in data:
    print(data[word])

else:
    print(word + " Doesn't exist in the dictionary")
