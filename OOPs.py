# Get index in the list of objects by attribute in Python
class x:
    def __init__(self,val):
        self.val = val

def getIndex(li,target):
    for index, x in enumerate(li):
        if x.val == target:
            return index
    return -1
li = [1,2,3,4,5,6]
a = list()
for i in li:
    a.append(x(i))

print(getIndex(a,5))
# Python program to build flashcard using class in Python
"""
class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + ' ( '+self.meaning+')'

flash = []
print("welcome to flashcard application")

while(True):
    word = input('enter the you want add to flashcard : ')
    meaning = input('enter the meaning of the word : ')

    flash.append(flashcard(word,meaning))
    option = int(input('enter 0 , if you want to add another flashcard : '))

    if (option):
        break

print("\nYour flashcards")
for i in flash:
    print(">",i)

"""
# How to count number of instances of a class in Python?
class geeks:
    counter = 0
    def __init__(self):
        geeks.counter += 1

g1 = geeks()
g2 = geeks()
print(geeks.counter)
# What is a clean, Pythonic way to have multiple constructors in Python?
class example:
    def __init__(self):
        print('One')
    def __init__(self):
        print('Two')
    def __init__(self):
        print('Three')
e = example()
# How to Change a Dictionary Into a Class?
class dict2class(object):

    def __init__(self,mydict):
        for key in mydict:
            setattr(self,key,mydict[key])

if __name__ == "__main__":
    mydict = {"Name": "Geeks","Rank":"1234","Subject":"Python"}
    result= dict2class(mydict)

    print('After converting dictionary to class : ')
    print(result.Name,result.Rank,result.Subject)
    print(type(result))
# Student management system in Python
class Student:
    def __init__(self,name,rollno,m1,m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    # function to create and append new student
    def accept(selfself,Name,Rollno,Marks1,Marks2):
        ob = Student(Name, Rollno, Marks1,Marks2)
        ls.append(ob)
    # function to display student
    def display(self,ob):
        print('Name :',ob.name)
        print("RollNo :",ob.rollno)
        print('Marks1 :',ob.m1)
        print('Marks2 :',ob.m2)
        print("\n")
    # search function
    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i

    # delete function
    def delete(selfself,rn):
        i = obj.search(rn)
        del ls[i]

    # update function
    def update(self,rn,No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll

ls =[]
obj = Student("",0,0,0)

print("\nOperations Used")
print("\n1.Accept Student Details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of a Student\n5.Update Student Details\n6.Exit")


obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)

print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])


print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])

obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])


obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])

print("Thank You !")

#How to create a list of object in Python class
class itess:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
list1 = []
# appending instannce to list
list1.append(itess('Ramesh',2))
list1.append(itess('Ganesh',40))
list1.append(itess('John',32))

for obj in list1:
    print(obj.name,obj.roll,sep=" ")

print()
print(list1[0].name)
print(list1[2].name)
print(list1[1].roll)