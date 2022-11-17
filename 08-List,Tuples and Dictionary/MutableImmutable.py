MyList=[1,2,3,4,5,6]
MyTuples=(1,2,3,4,5,6)
MyString='1,2,3,4,5,6'
MyDictionary={1:'A',2:'B',3:'C',5:'D'}
print("Initilize Memory Location ")
print("List ",id(MyList))
print("Tuples ",id(MyTuples))
print("Strings ",id(MyString))
print("Dictionary ",id(MyDictionary))
#Lets modify these structes
MyList.append(7)
MyTuples+='7',
MyString+='7'
MyDictionary[6]='E'
#Lets print memory address again
print('Modified Memory location')
print("List ",id(MyList))
print("Tuples ",id(MyTuples))
print("Strings ",id(MyString))
print("Dictionary ",id(MyDictionary))
