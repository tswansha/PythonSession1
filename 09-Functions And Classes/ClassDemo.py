class Person:
    #Attributes of the person
    name='Thilina'
    age=39
    salary=1000.0

    #Create custom constructor or init class
    def __init__(self,per_name,per_age,per_salary):
        self.name=per_name
        self.age=per_age
        self.salary=per_salary

    #Operations of person class
    def GettingOld(self,addedAge):
        self.age=self.age+addedAge

    def SalaryIncrement(self,Increment):
        self.salary=self.salary+Increment

#Create object using custom __init__ method 
P1=Person("Ravi",40,5000)
#print attribute
print("name= ",P1.name)
print("age= ",P1.age)
print("Salary =",P1.salary)
#Add 5 for age
P1.GettingOld(5)
#Add 2000 for salary
P1.SalaryIncrement(2000)
print("name= ",P1.name)
print("age= ",P1.age)
print("Salary =",P1.salary)
