

#----------------------------------------------------------------LAB 1 & 2--------------------------------------------------------------------------*3

#Q1._Ankit_Dagar
#Q.1:Check whether  a number is even or odd.
a=int(input("Enter A number : -"))
if a/2==0:
    print("Number is Even ")
else:
    print("Number is Odd ")

#Q2._Ankit_Dagar
#2.check whether an entered year  is leap year  or not.
a=int(input("Enter the year "))
if a%4==0 and a%100!=0:
    print("Is a Leap Year")
elif a%100==0:
    print("Is a LEAP year")
elif a%4!=0:
    print("Is a not Leap Year")
else:
    print("Is not LEAP year")

#Q3._Ankit_Dagar
#Q.3:write a program to check whether a character is vowel or consonants.
ch=input("Enter a Character :- ")
if(ch=='a' or ch=='A'or ch=='e'or ch=='E'or ch=='i'or ch=='I'or ch=='o'or ch=='O'or ch=='u'or ch=='U'):
    print(ch," is a Vowel")
else:
    print(ch,"is a consonant")


#Q4._Ankit_Dagar
#4. write a program to find the smallest of two numbers.
a=int(input("Enter first number :- "))
b=int(input("Enter second number :- "))
if a>b:
    print("First Number is Greater.")
elif b>a:
    print("Second Number is Greater")
else:
    print("Both are equal.")

#Q5._Ankit_Dagar
#Q.5:Find the Factorial of a number .
a=int(input("Enter A Number for FACTORIAL :- "))
m=1

if a<0:
    print("Factorial do not Exist.")
elif a==0:
    print("Fatorial of 0, is 1.")
else:
    for i in range(1,a+1):
        m=m*i
        print (m)

#Q6._Ankit_Dagar
#Q.6:Write a program  to print this patterns.
num=int(input("Enter a number :- "))

for i in range(num):
    for j in range((num-i)-1):
        print(end=" ")
    for j in range(i+1):
        
        print("*", end=" ")
print()

#Q7._Ankit_Dagar
#Q.7:Write a program  to print  this series .
#1 1  2 3 5 8 13 that is Fibbonacci series
a=int(input("Enter number of terms :- "))

b=0
c=1

for i in range(a):
    m=b+c
    b=m
    print(m)

#Q8._Ankit_Dagar
#Q.8:Check Whether a number is prime or not.
n=int(input("Enter a Number:"))

for i in range(2,n):
    if n%i==0:
        print(n,"is a Non-Prime Number")
        break
    if n%i!=0:
        print(n,"is a Prime Number")
        break

#Q9._Ankit_Dagar
#Q.9: Make  a simple  Calculator.
def sum(x,y):
    return x+y
def product(x,y):
    return x*y
def fact(x):
    fact=1
    i=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

def diff(x,y):
    if x>y:
        return x-y
    else:
        return y-x

def div(x,y):
    return float(x/y)

def lcm(x,y):
    if x>y:
        z=z
    else:
        z=y
    
    while True:
        if z%x==0 and z%y==0:
            lcm=z
            break
        z=z+1
    return lcm


p=int(input("Enter Password:- "))
if p==0000:
    print("1.SUM")
    print("2.PRODUCT")
    print("3.FACTORIAL")
    print("4.DIFFERENCE")
    print("5.DIVIDE")
    print("6.LCM")
    
    n=int(input("Enter Your Choice"))
    if n==1:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Sum is",sum(a,b))
    elif n==2:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Sum is",product(a,b))
    elif n==3:
        a=int(input("Enter Number:"))
        print("Factorial is",fact(a))
    elif n==4:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Difference is",diff(a,b))
    elif n==5:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Division is",div(a,b))
    
    elif n==6:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("LCM is",lcm(a,b))
else:
    print("Invalid Password")



#----------------------------------------------------------------LAB 3--------------------------------------------------------------------------*3

#Q1.Ankit_Dagar
#Q.1:WAP to demonstrate while loop with else statement.
i = 2
m = 2
while i == m:
    i += 1
    k=i
    print(k)
else: # Not executed as there is a break
    print("No Break")


#Q3._Ankit_Dagar
#Q3.Print 1st 4 even numbers (use continue statement).
n=int(input("Enter Range:"))
for i in range(1,n):
    if i%2==0:
        print(i)
    if i%2!=0:
        continue

#Q5.Ankit_Dagar
#Q.5:Write a Python program to calculate the length of a string.
n=int(input("Ankit Dagar"))
for i in range(1,n):
    if i%2==0:
        print(i)
    if i%2!=0:
        continue

#Q6._Ankit_Dagar
#Q6.Write a Python program to count the number of characters (character frequency) in a string
A="Ankit Dagar"
count=0
for i in A:
    if i=='a':
        count=count+1
print("Number of A in String is",count)


#Q7._Ankit_Dagar
#Q7.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#If the string length is less than 2, return instead of the empty string.
str=input("Enter a String:")
len=len(str)
if len<=2:
    print("Not Valid")
else:
    print(str[0]+str[1]+str[count-2]+str[count-1])

#Q8._Ankit_Dagar
#Q8.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself#
str=input("Enter a String:")
a=str[0]
str1=str.replace(a,"$")
print("Final String is ",a+str1[1:])


#Q9._Ankit_Dagar
#Q9.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str=input("Enter First String:")
str1=input("Enter Second String:")

a=str+" "+str1
print("Total String is",a)

b=str.replace(str[0],str1[0])
c=str1.replace(str1[0],str[0])

print("Final String after Replacement is",b+' '+c)

#Q10._ANKIT_DAGAR
#Q10.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
str=input("Enter a String:")
str1=""
count=len(str)
if count>2:
    if str[-3:]=='ing':
        str=str[0:3]+"ly"
    else:
        str=str+"ing"
        print(str1)

#----------------------------------------------------------------LAB - 4----------------------------------------------------------------------------*#

#Q1
a=("Hi")

#Q2
a=("Hi",2,2.3)
print(a)

#Q3
a=(1,3,4,12)
print(a[0])

#Q5
a=(1,4,5,12,34)
x=int(input("Enter Number to add in the Tuple:"))
a=a+(x,)
print(a)

#Q6
tup=("Hi","Dags")
str=''.join(tup)
print(str)

#Q7
tup=(1,2,3,4,5,6,7,8,9,10)
print(tup[3])

#Q9
tup=(1,2,3,4,1)
a=tup[0]
for i in tup:
    if i==a:
        print("Element",a,"found")
    else:
        continue


#Q10
tup=(1,2,3,4,5)
x=int(input("Enter a Number:"))
for i in tup:
    if i==x:
        print("Yes",x,"is present")
    else:
        continue

#Q11
list=[1,1,2,3]
tup=tuple(list)
print(tup)

#Q12
tup=(1,100,123,4,34,78,98)
tup=tup[:3]+tup[4:]
print(tup)

|#Q13
tup=(3,5,1,100,45,12,65)
tup=tup[:2]+tup[3:]
print(tup)

#Q14
tup=(2,5,12)
x=int(input("Enter Number to find Index:"))
for i in tup:
    if i==x:
        print("Number",x,"found at",i-1,"location")
    else:
        continue

#Q15
tup=(12,3,45,12)
sum=0
for i in tup:
    sum=sum+1
print("There are",sum,"elements")

#----------------------------------------------------------------LAB - 5--------------------------------------------------------------------------*#
#Q1.Ankkit_Dagar
a=["hi"]
print(a)

#Q2.Ankkit_Dagar
a=["Hi",2,2.3]
print(a)


#Q3.Ankit_dagar
tup=(23,46,"False",49.5,"true","Apple","Mango")
print(tup)

#4.Ankit_Dagar
tup=(23,46,"False",49.5,"true","Apple","Mango")
y=list(tup)
y[1]="orange"
tup=tuple(y)
print(tup)


#Q5.Ankit_dagar
tup=('a','b','c','d','e')
str="     ".join(tup)
print(str)

#Q6.Ankit_dagar
tup=(23,"Kullz BOizz",46,"False",49,"Paris","true","Apple","Mango")
print(tup[3]+" "+tup[-4])

#Q8._Ankit_Dagar
#Q8.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself#
str=input("Enter a String:")
a=str[0]
str1=str.replace(a,"$")
print("Final String is ",a+str1[1:])

#Q7.Ankit_dagar
from copy import deepcopy
tup=(23,"Kullz BOizz",46,"False",49,"Paris","true","Apple","Mango")
tups=deepcopy(tup)
print(tups)

#9.Ankit_Dagar
a=input("Enter a number:- ")
tup=('a','b','c','d','e')
a=list(tup)
for a in tup:
    print("Is PRESENT in the Tuple.")

#10.Ankit_Dagar
tup=['a','b','c','d','e']
a=tuple(tup)
print(a)

#Q11.Ankkit_Dagar
tup=('a','b','c','d','e')
a=list(tup)
a.remove('b')
a=tuple(a)
print(a)

#----------------------------------------------------------------LAB 6----------------------------------------------------------------------------*#


#Q1. Create a dictionary as discussed in the class

#Q2. Access the key for the value 1964 both without using get function and with using get function.

#Q3. Change the value of the model to Eco Sport.

#Q4. Add the items model number m001 and color as red in the dictionary.

#Q5.print the dictionary keys, values, both key-value pairs.

#Q6. Check if the model eco sport exists or not.

#Q7. Remove the item with the key brand from the dictionary using two different functions.

#Q8.Before removing the item create two duplicate copies using two duplicate functions.

#ANSWER – LAB - 06
#_All_Answers
a={"brand":"farari","model":"mustang","year":"1964"}
print(a)
for i in a.values(): #print all the values in the dectionary
    print(i)
for x,y in a.items(): # print key and dictoney both
    print(x,y)
if "model"in a :
    print("value founded")
a["name"]="ankit"  #insert new key and value in dectionary
print(a)
a.pop("name") #delete name key and value
print(a)
a.popitem() #remove last inserted value from dectionary
print(a)
a["model"]="halwa"
print(a)

#del a means del dectionary
b=a.copy() #copy command to copy dictonary
print(b)
c=dict(a) #another copy method to copy dictonary
print(c)



#----------------------------------------------------------------LAB 7----------------------------------------------------------------------------*#

#LAB-07_.Ankkit_Dagar

#Q1
a={"":""}
print(a)

#Q2
a={"A":"10","B":"20"}
print(a)
#Q3
a={"A":"Dagar","B":"10"}
print(a)
#Q4
print(a)
#Q5
for i,j in a.items():
    print(i,j)

#Q6
a.pop("A")
print(a)
#Q7
del a

#Q8
b={"A":"Dags","B":"10"}
for i in b.values():
    print(i)

#Q9
if "id" in b :
    print("value Exixt")
else :
    print("Id is ABSENT ")

#Q10
b["A"]="Dags!!"
print(b)

#Q11
b["C"]="M.A.D."
print(b)

#Q12
c={}
for i in range(1, 10):
    c[i]=i**2
    print(c)

#Q13
d1={"A":1,"B":2,}
d2={"C":3,"D":4,}
d3={"E":5,"F":6,}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
    print(d4)

#Q14
i=0
w={1:1,2:2,3:3,4:4,5:5,6:6}
for a in w.values():
    i=a+i
    print(i)

#Q15
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
d5={}
for i in (dic1,dic2,dic3):
    d5.update(i)
    print(d5)

#Q16
z=d5[3]
print(z)

#Q17
dict1={}
for key in range(1,15):
    dict1[key]=key*key
    print(dict1)


#Q18
a={}
f=1
for i in range(1,16):
    f=f*i
    a[i]=f
print(a)

#----------------------------------------------------------------LAB 08----------------------------------------------------------------------------*#
#Q1) Ankit_Dagar
class triangle:
    
    def create_triangle(self,side1,side2,side3):
        self.a=side1
        self.b=side2
        self.c=side3
        print(self.a)
    
    def print_slide(self):
        print(self.a)
        print(self.b)
        print(self.c)

obj=triangle()
obj.create_triangle(1,2,3)
obj.print_slide()

#Q2) Ankit_Dagar
class  alpha:
    
    def get_string(self,alpha1,alpha2):
        self.a=alpha1
        self.b=alpha2
    
    def print_String(self):
        print(self.a)
        print(self.b)

obj2=alpha()
obj2.get_string(a,b)
obj2.print_String()

#Q3 Ankit_Dagar
class rectangle:
    def rect_values(self,l,w):
        self.lenght=a
        self.width=b
    
    def perimeter(self):
        self.per=2*(self.lenght+self.width)
        return(self.per)

a=int(input("enter a "))
b=int(input("enter b "))

r1=rectangle()
r1.rect_values(a,b)
k=r1.perimeter()
print("perimeter is",k)

#Q4 Ankit_Dagar
class circle:
    
    def circle_area(self,r):
        self.radius=r
        self.area=(3.14)*(r)*(r)
        return(self.area)
    
    def circle_perimeter(self):
        self.perimeter=2*(3.14)*(r)
        return(self.perimeter)

r=int(input("Enter the radius of Circle, r = "))

obj4=circle()
k=obj4.circle_area(r)
m=obj4.circle_perimeter()
print("The AREA of the circle is :- ",k)
print("The PERIMETER of the Circle is :- ",m)

#Q5 Ankit_Dagar
class circle:
    
    def getArea(self,r):
        self.radius=r
        self.area=(3.14)*(r)*(r)
        return(self.area)
    
    def getCircumference(self):
        self.perimeter=2*(3.14)*(r)
        return(self.perimeter)

r=float(input("Enter the radius of Circle, r = "))

obj4=circle()
k=obj4.getArea(r)
m=obj4.getCircumference()
print("The area of the circle is :- ",k)
print("The Circumference of the Circle is :- ",m)

#Q6 Ankit_dagar
class Temprature:
    F1=0
    F2=0
    C1=0
    C2=0
    def convertFahrenheit(self,F1,C2):
        self.fra1=F1
        self.cel2=C2
    
    def convertCelsius(self):
        self.fra2=(9/5)*(self.cel2)+32
        self.cel1=(5/9)*((self.fra1)-32) #(°F − 32) × 5/9 = °C
        print("\nThe Fahrenheit is ",self.fra2)
        print("The celcius ",self.cel1)

F1=int(input("Enter Fahrenheit temp :- "))
C2=int(input("Enter Celcius temp :- "))

obj6=Temprature()
m=obj6.convertFahrenheit(F1,C2)
k=obj6.convertCelsius()

#Q(7). Ankit_Dagar
class Student():
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll
        self.marks=marks
    
    def display(self):
        print ("\nThe NAME is :--> Ankit")
        print ("& Your ROLL is :--> 2K18CSUN01053 ")
    
    
    
    def setAge(self,age):
        self.age=age
        age=input("Enter Your Age :- ")
    
    def setMarks(self,marks):
        self.marks = marks
        marks=input("Enter you mark :- ")


name=((()))
roll= ()
marks=((()))
age=((()))

obj10=Student(name,roll)
obj10.setAge(age)
obj10.setMarks(marks)
obj10.display()
obj10.setAge(age)
obj10.setMarks(marks)

#Q.(8) Ankit_Dagar
class Time:
    
    def _inti_(self):
        self.hour1=hour1
        self.mins1=mins1
        self.hour2=hour2
        self.mins2=mins2
    
    def addTime(self):
        self.hour=(self.hour1)+(self.hour2)
        self.mins=(self.mins1)+(self.mins2)
        if (self.mins)/60 >= 1:
            m=((self.mins)/60)
            k=(self.hour)+(int(m))
            l=((m)-(int(m)))*60
            print("The Total is ",k,"Hours & ",int(l),"Minutes")
        else:
            print("Total is ",self.hour,"hour",self.mins,"minutes")

def DisplayMinute(self):
    self.mins3=(self.hour*60)+(self.mins)
    print("\nThe total mintues ",self.mins3,"minutes")

hour1=int(input("Enter First Hour :- "))
mins1=int(input("Enter First Minutes :- "))
hour2=int(input("\nEnter Second hours :- "))
mins2=int(input("Enter Second Minutes :- "))

obj12=Time()
obj12._inti_()
obj12.addTime()
obj12.DisplayMinute()

#Q9 Ankit_Dagar

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
print(py_solution().reverse_words('BEST IS ANKIT-DAGAR')).


#----------------------------------------------------------------LAB 09----------------------------------------------------------------------------*#
#Q1) Ankit_Dagar

#Lab-10

#Lab10

#Q1.Ankkit_Dagar
class Animal:
    def __init__(self, leg):
        self.leg = leg
    
    def printleg(self):
        print(self.leg)

class tiger:
    x = Animal("4")
    print("Tiger has leg:- ", end="")
    x.printleg()
class dog:
    x = Animal("4")
    print("Dog has leg:- ", end="")
    x.printleg()

#Q2.Ankkit_Dagar
class Employee:
  def __init__(self, desg):
    self.desg = desg

  def printdesg(self):
    print(self.desg)

class engineer:
    x = Employee("Enginner")
    print("This has a designation of:- ", end="")
    x.printdesg()
class manager:
    x = Employee("Manager")
    print("This has a designation of:- ", end="")
    x.printdesg()

#Q3.Ankkit_Dagar
class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')
print(MyClass.a)
print(MyClass.func)
print(MyClass.__doc__)


#Q4.Ankkit_Dagar
class Parent(): 
    def __init__(self): 
        self.value = "Inside Parent" 
    def show(self): 
        print(self.value) 
class Child(Parent): 
    def __init__(self): 
        self.value = "Inside Child"
    def show(self): 
        print(self.value)  
obj1 = Parent() 
obj2 = Child() 
  
obj1.show() 
obj2.show()


#Q5.Ankkit_Dagar
class Class1:
    def m(self):
        print("In Class1")
class Class2(Class1):
    def m(self):
        print("In Class2")
class Class3(Class1):
    def m(self):
        print("In Class3")
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
obj = Class4()
obj.m()

Class2.m(obj)
Class3.m(obj)
Class1.m(obj)
