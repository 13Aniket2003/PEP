### Given a string, which is the company name in lowecase letters, yours task is to find the top three most common characters in the string.
### print the three most common characters along with their occurance count. sort in descending order of occurance count. if the occurance count
### is the same, sort the characters in alphabeticals order.
### input:--> aabbbccdef
### output:--> b 3  a2  c2

# company_name=input()
# occurance=[]
# c=[]
# for char in company_name:
#     if char not in occurance:
#         a=company_name.count(char)
#         c.append([char,a])
#         occurance.append(char)
# c.sort()                                         ### first sorting the character
# c.sort(key=lambda x:x[1], reverse=True)          ### then sorting the number
# for i in range(3):
#     print(c[i][0],c[i][1])
#-------------------------------------------------------------------------------------------------------------------------------------------------

#### Data class decorator is a feature introduced in python that provides a concise way to define classes primarily intended to store data. 
#### It automatically generates several special methods, such as init,repr, and eq, based on the class attributes you define. 
#### This simplifies the proccess of creating and working with data.

# from dataclasses import dataclass
# @dataclass
# class person:
#     name:str
#     age:int
#     profession:str

#-------------------------------------------------------------------------------------------------------------------------------------------------

#### The @dataclass decorator automatically generates the following methods for you: 
#### 1. init(): initializes the objects and assigns the provided values to the attributes. 
#### 2. repr(): provides a string representation of tghe object. 
#### 3. eq(): implement equality comaprision between two objects of the class based on their attributes.

#### example input person name , age, profession and priting that data

# person1=person('krish',17,'SE')
# print(person1)
# print(person1.age)
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#### example rectangle lenth,width,color

#from dataclasses import dataclass
# @dataclass
# class rectangle:
#     width:int
#     height:int
#     color:str='white'
# rectangle1=rectangle(12,14)
# rectangle2=rectangle(13,15,'red')
# print(rectangle2.color)

#---------------------------------------------------------------------------------------------------------------------------------------------

#### example frozen argument make the class read-only(immutable) afetr it has been created. 
#### Later on if we try to change it , it will throw error cause it is in frozen state.

#### example of frozen argument

# from dataclasses import dataclass
# @dataclass(frozen=True)
# class point:
#     x:int
#     y:int
# point=point(3,4)
# print(point)
# print(point.x,point.y)
# point.x=12                       ## this will throw error as it is in frozen state
# print(point.x)                   ## after print it will throw
#------------------------------------------------------------------------------------------------------------------------------------------------

#### Dataclass Inheritance

#### example printing employee name

# from dataclasses import dataclass
# @dataclass
# class person:
#     name:str
#     age:int

# @dataclass
# class employee(person):
#     employee_id:int
#     department:str

# person=person('krish',17)
# employee=employee('krish',17,123,'SE')

# print(employee.name)
#-------------------------------------------------------------------------------------------------------------------------------------------------

#### Nested Dataclass

#### example printing city address of employee 
# from dataclasses import dataclass
# @dataclass
# class address:
#     street:str
#     city:str
#     zip_code:int

# @dataclass
# class person:
#     name:str
#     age:int
#     address:address

# address=address('phagwara','punjab',1444011)
# person=person('Bad',27,address)

# print(person.address.city)
#----------------------------------------------------------------------------------------------------------------------------------------------

#### Create a class student. Take input of name,enrollment no, roll no. 
#### Create a class for marks where values should be start sem,mid sem and end sem. 
#### create Interview score class where store the interview score, resume score, technical score, knowledge score.
#### Map the end sem result with interview score.

#from dataclasses import dataclass
# @dataclass
# class student:
#     name:str
#     enrollment_no:int
#     roll_no:int

# @dataclass
# class marks(student):
#     start_sem:int
#     mid_sem:int
#     end_sem:int

# @dataclass
# class interview_score(marks):
#     resume_score:int
#     technical_score:int
#     knowledge_score:int
# name=input("enter the name: ")
# enroll=int(input("enter the enroll no.: "))
# roll=int(input("enter the roll no: "))
# start=int(input("enter first sem marks: "))
# mid=int(input("enter second sem marks: "))
# end=int(input("enter third sem marks: "))
# resume=int(input("enter resume score: "))
# technical=int(input("enter technical score: "))
# knowledge=int(input("enter knowledge score: "))
# student_full=interview_score(name,enroll,roll,start,mid,end,resume,technical,knowledge)
# print("Name: ",student_full.name,"Enroll no: ",student_full.enrollment_no,"Roll no: ",student_full.roll_no,"start sem: ",
# student_full.start_sem,"midsem: ",student_full.mid_sem,"end sem: ",student_full.end_sem,"resume score: ",
# student_full.resume_score,"Technical score: ",student_full.technical_score,"knowledge score :",student_full.knowledge_score)
#---------------------------------------------------------------------------------------------------------------------------------------------------

#### Inheritance

# class car:
#     def _init_(self, windows, doors, enginetype):
#         self.windows = windows
#         self.doors = doors
#         self.enginetype = enginetype

#     def driving(self):
#         print("car is used for driving")


# class Audi(car):
#     def _init_(self, windows, doors, enginetype, horsepower):
#         super()._init_(windows, doors, enginetype)
#         self.horsepower = horsepower

#     def selfdriving(self):
#         print("It is a self driving car")


# audiq7 = Audi(4,5,"Diesel", 200)

# print(audiq7.horsepower)
# print(audiq7.windows)
# audiq7.driving()
# audiq7.selfdriving()

# car1 = car(4,5,"Diesel")
# print(car1)
# print(audiq7)

# print(dir(audiq7))
# print(dir(car1))
#----------------------------------------------------------------------------------------------------------------------------------------------

#### Class methods and Class variables

# class car:
#     base_price=100000        # Class variables
#     def __init__(self,windows,doors,power):
#         self.windows=windows
#         self.door=doors
#         self.power=power
#     def what_base_price(self):
#         print("the base price is {}".format(self.base_price))
#     @classmethod
#     def revise_base_price(cls,inflation):
#         cls.base_price=cls.base_price+cls.base_price*inflation
# car.revise_base_price(0.10)
# print(car.base_price)
# car1=car(4,5,2000)
# print(car1.base_price)
# car1.revise_base_price(0.07)
# print(car1.base_price)
#------------------------------------------------------------------------------------------------------------------------------------------------

#### Python OOPS --> Public, Private, protected

## Public class

# class car():
#     def __init__(self, windows, doors, enginetype):
#         self.windows = windows
#         self.doors = doors
#         self.enginetype = enginetype
# audi = car(4,5,"Diesel")
# audi.windows = 5
# print(audi.windows)
#--------------------------------------------------------------------------------------

## Protected class

# class car():
#     def __init__(self, windows, doors, enginetype):
#         self.windows = windows
#         self.doors = doors
#         self.enginetype = enginetype
# class truck(car):
#     def __init__(self, windows, doors, enginetype,horsepower):
#         super().__init__(windows,doors,enginetype)
#         self.horsepower=horsepower
# Truck=truck(4,4,"diesel",4000)
# print(dir(Truck))      # dir ---> directory / attributes
# truck._doors=5
# print(truck._doors)
#-------------------------------------------------------------------------------------

## Private class

# class car():
#     def __init__(self, windows, doors, enginetype):
#         self.__windows = windows
#         self.__doors = doors
#         self.__enginetype = enginetype
# audi=car(4,4,"diesel")
# audi._car__doors=5
# print(dir(audi))
# print(audi._car__doors)
#------------------------------------------------------------------------------------------------------------------------------------------------

#### Create a class student. Take input of name,enrollment no, roll no. 
#### Create a class for marks where values should be start sem,mid sem and end sem. 
#### create Interview score class where store the interview score, resume score, technical score, communication score.
#### Map the end sem result with interview score.
#### compare those marks if the student get marks more than 70 is pass else fail and if 0 he is absent

# from dataclasses import dataclass
# @dataclass
# class student:
#     name:str
#     enrollment_no:int
#     roll_no:int

# @dataclass
# class marks(student):
#     start_sem:int
#     mid_sem:int
#     end_sem:int

# @dataclass
# class interview_score(marks):
#     resume_score:int
#     technical_score:int
#     knowledge_score:int
# name=input("enter the name: ")
# enroll=int(input("enter the enroll no.: "))
# roll=int(input("enter the roll no: "))
# start=int(input("enter first sem marks: "))
# mid=int(input("enter second sem marks: "))
# end=int(input("enter third sem marks: "))
# resume=int(input("enter resume score: "))
# technical=int(input("enter technical score: "))
# knowledge=int(input("enter knowledge score: "))
# student_full=interview_score(name,enroll,roll,start,mid,end,resume,technical,knowledge)
# print("Name:",student_full.name,",Enroll no:",student_full.enrollment_no,",Roll no: ",student_full.roll_no,",start sem: ",
# student_full.start_sem,",midsem: ",student_full.mid_sem,",end sem: ",student_full.end_sem,",resume score: ",
# student_full.resume_score,",Technical score: ",student_full.technical_score,",knowledge score :",student_full.knowledge_score)
# class student_absent(Exception):
#     pass

# try:
#     if student_full.end_sem==0:
#         raise student_absent
#     elif student_full.end_sem>=70:
#         print("The student is passed")
#     else:
#         print("failed")
# except student_absent:
#     print("The student is absent")
# finally:
#     print("All done")
#------------------------------------------------------------------------------------------------------------------------------------------

#### Assert:--> Python provides the assert statement to check if a given logical expresssion is true or false.
### Program execution proceeds only if the exception is true and raise the AssertionError when it is false. 
### the following code shows the usage of the assert statement.

# try:
#     num = int(input("enter a number: "))
#     assert num%2==0
#     print("The number is even")
# except AssertionError:
#     print("please enter even number")
#--------------------------------------------------------------------------------------------------------------------------------------------

#### Django:--> the main reason of behind djnago exisytance is that django inherited pythons batteries included approach. 
# It also include pre-made moduels and applications.
# Like user auhtentication,routes and views, templates admin interface , robust security and support for multiple database backends.
# Default database--> DB.SQL lite 3 and it can also be transfer to other databases too. 
# it is ridiculously fast. It was designed to help developers take applications from concept to completion as quickly as possible.
# It is fully loaded, that is incluydes dozens of extras you can us eto handle. It is reassuringly secure. 
# MTV framework--> Model-data access layer--- this deals with access,validation and relationship among data. 
# Models are python classes that mediate between django and ORM and the databases. 
# Template-presentation layer---tHis deals with how data is displayed to the client. 
# view-Business logic layer--- It is a bridge b/w models and templates. it access model data and redirects it to a templates for presentation.
# Unlike traditional MVC, Django views data what we see.

#       ----------------------------------------------------------------------  
#       |       Model --------------------------------------> Template       |
#       |   (object,relational,mapping,orm)                  (display,logic) |
#       |       ^                                                    |       |
#       |       |   (create,update,delete)                           |       |
#       |       |                                 View               |       |
#       |       |--------------------------- business,logic <--------|       |
#       ----------------------------------------------------------------------

#       ----------------------------------------------
#       |               ---------->  SQL             |
#       |               |                            |
#       |           Databases                        |
#       |               |                            |
#       |               ------------> Django ORM     |
#       ----------------------------------------------
             
# Orm provides a bridge b/w relational databases tables, relationships and frields in python object.
