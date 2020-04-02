#BASIC PYTHON WALKTHROUGH

'''
Written by: Asim Mahat
            April 2,2020
'''

from math import *

# 1.PRINTING OUT SOME STRUCTURES
print("     |")
print("    /|\")
print("   / | \")
print("  /  |  \")

#storing data in variables
name= "Asim"
colz="Kathmandu Univeristy"
 
print(name+ " studies in " +colz)

# 2. USING INBUILT FUNCTION
code="Coding"
print(code.upper()+" is cool") #the variable code is changed into uppercase

#printing out the length
print(len(code))

#using index which starts from zero
print(code[0])#accessing first character in the string

#using vice versa-->finding the index value of "C"
print(code.index("C"))

#using replace function to replace the string
print(code.replace("Coding","Programming"))

# 3.WORKING WITH NUMBERS
#Addition
print(2.3+ 4.5)
#Subtraction
print(2.3-4.5)
# all operations at once
print(3*(4+5))
#converting the number into string
num=10
print(str(num)+ " is first two digit number")

#most common use math funcitons
#absolute value
print(abs(num))
#power
print(pow(2,3))
#maximum value
print(max(10,9))
#minimum value
print(min(10,9))
#round
print(round(5.7))
#floor and ceiling function
print(floor(5.7))
print(ceil(5.7))
#square root
print(sqrt(36))

# 4.GETTING INPUT FROM USER

name = input("Enter your name: ")
colz = input("Enter your colz: ")
print("Your name is " + name+ " and you study in "+colz)

# 5.BUILDING A BASIC CALCULATOR THAT PERFORMS ADDITION
num1=input("Enter a number:")
num2=input("Enter another number:")

result=float(num1)+float(num2)#changing the string into the integer number
print(result)

# 6.BUILDING A MAD LIB GAME

color=input("Enter a color:")
plural_noun=input("Enter a plural noun:")
celebrity=input("Enter a celebrity:")
sports=input("Enter your favorite sports:")

print("\nRoses are "+color)
print(plural_noun+" are blue")
print("I love "+ celebrity)
print("I hate "+ sports )

'''
'''
# DATA STRUCTURES IN PYTHON
# 7.WORKING WITH LISTS

sports=["football","basketball","volleyball","table-tennis","long-tennis","Badminton"]
print(sports)
print(sports[0])#printing element at index 0
print(sports[1:])#printing all elements from index 1
print(sports[1:3])#printing from index 1 to index 3

#different list funtions

numbers=["1","5","9","4","6","43","21"]
sports=["football","basketball","volleyball","table-tennis"]

# print(numbers)
# print(sports)
# sports.append("golf") #appending golf at end of sports list
# print(sports)
# sports.insert(1,"cricket") #insert cricket
# print(sports)
# sports.pop() #pops out the last element
# print(sports)
# print(sports.index("basketball"))#finding the index of basketball
# sports.remove("basketball") #removes basketball
# print(sports)
# sports.sort()#sorting in alphabetical order
# print(sports)


# 8.WORKING WITH TUPLES (SIMILAR TO THE LIST)
#tuples are immutable that means it cannot be changed
#in tuples parenthesis is used instead of square bracket
#for permanent data tuples are used

point_in_space=(2,7)
name_of_students=("Kevin","David","John","Mike")
print(point_in_space[2])
print(name_of_students[2])


# 9. WORKING WITH FUNCTIONS
#collection of instruction that performs the specific task
#organize the code into different chunks that have particular objective

#function that says "Hello"
def say_hello(name,colz,age):
    print(" Hello !!! "+name +" you are from "+colz + " and you are "+ str(age))

say_hello("Mike","Stanford",23)#here the function is called
say_hello("Asim","Kathmandu Univeristy",21)

 
# 10.RETURN STATEMENTS IN PYTHON FUNCTIONS
#getting information back from the function

def cube(a):
    return a*a*a
    #return keyword breaks out of the function
result=cube(3)
print(result)

# 11.USING IF STATEMENTS

#checking if statement with boolean value
#checking all necesssary condition TT TF FT FF

is_male=False
is_tall=True

if is_male or is_tall: # we can use "or" "and" operation
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are male and not tall")
elif not(is_male) and (is_tall):
    print("You are not male but tall")
else:
    print("You are not a male")


# 12.IF STATEMENTS AND COMPARSION

#making a function that finds greatest among the three numbers
def max_num(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b 
    else:
        return c

print(max_num(200,300,150))

# 12. MAKING A BASIC CALCULATOR

number_1=float(input("Enter the first number:"))
operator=input("Enter the operation:")
number_2=float(input("Enter the second number:"))

if operator=="+":
    print (number_1 + number_2)

elif operator=="-":
    print (number_1 - number_2)

elif operator=="/":
    print (number_1 / number_2)

elif operator=="*":
    print(number_1 * number_2)

else:
    print("Invalid operator")


# 13. USING DICTANORIS IN PYTHON
#word=key and  actual defination=value
#program to convert three digit month name into the real month name
#key value pairs
# "key_values"="actual meaning" ,key value can be anything

convert_month={ "Jan": "Janaury",
                "Feb":"Februray",
                "Mar":"March",
                "Apr":"April",
                "May":"May",
                "Jun":"June",
                "Jul":"July",
                "Aug":"August",
                "Sep":"September",
                "Oct":"October",
                "Nov":"November",
                "Dec":"December"
}
# print(convert_month["Jan"])
print(convert_month.get("Jan"))


# 14. WHILE LOOP IN PYTHON

#printing from one to fifty using a basic while loop

i=1
while i<=50:
    print(i)
    i += 1
print("We are out of the while loop")

# 15. BUILD A BASIC GUESSING GAME

secret_word="coding"
user_word=""
count =0
limit=3
out_of_guesses=False

while secret_word!=user_word and not(out_of_guesses):
    if count < limit:
        user_word=input("Enter your guess word:")
        count +=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("You are out of guesses, YOU LOSE !")
else:
    print("You have won !")


# 16. USING FOR LOOP

sports=["Football","Basketball","Cricket","Volleyball"]
for sport in sports:
    print(sport)
#for loop in index range
for index in range(2,10):
    print(index)

for index in range(5):
    if index==0:
        print("First Iteration")
    elif index==1:
        print("Second Iteration")
    elif index==2:
        print("Third Iteration")
    elif index==3:
        print("Fourth Iteration")
    else:
        print("Fifth iteration")


# 17.USING FOR LOOP TO WRITE A EXPONENT FUNCTION

def exponent(number,power):
    result=1
    for index in range(power):
        result=result*number
    return result

print(exponent(2,3))

# 18. 2D lists and nested for loops

grid=[
    [1,2,3],
    [4,6,8],
    [9,12,10]
]
print(grid[1][1])

#first of all rows is scanned and each element of row is printed
for row in grid:
    for col in row:
        print(col)



# 19. BASIC TRANSLTOR
# Here any vowel letter is changed into letter "z"

def transform(word):
    translator=""
    for letter in word:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translator=translator + "Z"
            else:
                translator=translator + "z"

        else:
            translator=translator+letter
    return translator

print(transform(input("Enter a word :")))

#20. CATCHING ERROR IN PYTHON
#try except block
#catiching invalid input using try accept block
try:
    # i=5/0
    number =int(input("Enter a number:"))
    print(number)
# except ZeroDivisionError:
    # print("Invalid Input-Divided by zero")
except:
    print("Invalid Input")


#21. READING FROM EXTERNAL FILE IN PYTHON
#read the file in other directories
#using python read command

open("filename.txt","modes") #you can put the file name or its path
#modes can be read,write append 
#lets store it in a variable
info= open("filename.txt","modes")
info.close()#closing a file


#22.WRITING THE FILE
#for reading and writing we can use pandas libraries



#23.MODULES IN PYTHON

#you can import different necessary modules in python
#import math
#import random
#import os
#import time and there are many mores


#OOP(OBJECT ORIENTED PROGRAMMING)
#24. CLASSES AND OBJECTS IN PYTHON
#it makes program more organized and more powerful
#when data-types in python cant cover , we should create our own datatype

class student:
    #initialize functiom
    def __init__(self,name,major,gpa,age,is_on_colz):

        #what attribute a student should have
        self.name=name
        self.major=major
        self.gpa=gpa
        self.age=age
        self.is_on_colz=is_on_colz

#class is the overview of what a student is, object is the actutal student

class teacher:

    def __init__(self,name,faculty,age,qualification):
        self.name=name
        self.faculty=faculty
        self.age=age
        self.qualification=qualification

teacher_1=teacher("Jones","Mechanical","42","Phd")
teacher_2=teacher("David","CS","39","Masters")

student_1=student("MIke","CS","3.0","21",False)
student_2=student("David","Arts","3.1","23",True)

#here student_1 ,student_2 ,teacher_1 and teacher_2 are objects

print(student_2.age)
print(student_1.is_on_colz)

print(teacher_1.name)
print(teacher_2.age)

 





     














    

 



