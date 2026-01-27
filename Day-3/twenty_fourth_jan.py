### Given the participants score sheet for your university sports day. you are required to find the runner-up score. you are given scores.
### store them in list and find the score of the runner-up.
### input format-
### the first contains total no. of contestants 'a'. The scond line contains an array of integers each separated by a space.
### constraints :-> 2<=a<=100
## output-----> print the runner-up score.

# a=int(input("enter the the no. of contestants: "))
# b=[]
# for i in range(a):
#     b.append(int(input("enter the scores: ")))
# print("the runner up score is: ", max(b)-1)
#-------------------------------------------------------------------------------------------------------------------------------------------------#

### dictionaries having names and age you have to sort the dictionary according to age basis in decending order take min 3 name and ages

# a={"harry":85,"Robin":22,"Kevin":73}
# s=dict(sorted(a.items(), key=lambda item:item[1],reverse=True))
# print(s)
#---------------------------------------------------------------------------------------------------------------------------------------------------#

### replace the particular element of a string str='abcdefgh' --> str='abcdxfgh'

# a=input("enter string: ")
# old_character=input("enter the character to be replaced: ")
# new_character=input("enter new character to be insert")
# result=a.replace(old_character,new_character)
# print(result)
#--------------------------------------------------------------------------------------------------------------------------------------------------#

### in a string if there any repeated letter print that repeated letter

# a=input("enter the string: ")
# repeate=[]
# for char in a:
#     if a.count(char)>1 and char not in repeate:
#         repeate.append(char)
# print(repeate)

# ## OR

# a=input("enter the string: ")
# r=set()
# for char in a:
#     if a.count(char)>1:
#         r.add(char)
# print(r)
#------------------------------------------------------------------------------------------------------------------------------------------------#

#### i have a str='this is good classroom', find l from the starting 5 letter, if found true else false

# a=input("enter string: ")
# b=a[:6]
# character_to_find=input("enter the character: ")
# if character_to_find in b:
#     print("prsent")
# else:
#     print("not present")
#--------------------------------------------------------------------------------------------------------------------------------------------------

### Boolean variables

# str=input("enter string: ")
# print(str.isalnum) # alpha-numeric i.e, alphabet true + numeric+alphabet true + numeric only true i.e, abc123 or 123 or abc
# print(str.isalpha)
# print(str.isdigit) # only whole number like 1,2,3
# print(str.istitle)
# print(str.isupper)
# print(str.islower)
# print(str.isspace)
# print(str.endswith)
# print(str.startswith)
# print(str.isnumeric) # for any number including fraction or roman number i.e., VII or 1/2
#------------------------------------------------------------------------------------------------------------------------------------------------

# insert in specific index in list

#list=["a",'b','c','c','e','f']
# ##list.insert(index,"value_to_be_insert")
# list.insert(3,"value_to_be_insert")
# print(list)
#----------------------------------------------------------------------------------------------------------------------------------------------------

### using extend method using to avoid nested list

# list.extend(['g','h'])
# print(list)
#-------------------------------------------------------------------------------------------------------------------------------------------------

### use of count function

# b=list.count('c')
# print(b)
#------------------------------------------------------------------------------------------------------------------------------------------------

### index(): return the index of the first occurance. start and end index are not necessary parameter

# # list.index(value,first_index,end_index)
# c=list.index('c',1,6)
# print(c)
#------------------------------------------------------------------------------------------------------------------------------------------------

### sets: it is an unordered collection data types that is iterable,mutable,and has no duplicate element. 
# python set class represent the mathematical notion of a set.this is based on a data structure known as a hash table

#set_var1={"average","iron","metal"}
# print(set_var1)
# print(type(set_var1)) # to check the type of variable whether it is int or float or bool or set or anything
# set_var1.add("sea") # to add value
# print(set_var1)
#set_var2={"average","metal","logic","math"}
#set_var2.intersection_update(set_var1) # intersection
#set_var2.difference_update(set_var1) # different
#print(set_var2)
#------------------------------------------------------------------------------------------------------------------------------------------------

### nested dictionary

# car1={'BMW':1758}
# car2={'Audi':1970}
# car3={'Nano':1895}
# car_type={'car1':car1,'car2':car2,'car3':car3}
#print(car_type)
#print(car_type['car2'])
#print(car_type['car1']['BMW'])
#---------------------------------------------------------------------------------------------------------------------------------------------------

### tuples

# my_tuple=("a","b0","c","d","d",1,2,3,4)
# print(my_tuple)
# type(my_tuple)
# print(my_tuple.count('d'))
# print(my_tuple.index('b0'))
#------------------------------------------------------------------------------------------------------------------------------------------------

###  Shallow copy

# lst1=[1,2,3,4]
# lst2=lst1.copy()
# print(lst2)
# lst2[1]=100
# print(lst1,lst2)
# ------------------------------------------------------------------------------------------------------------------------------------------------

### shallow copy nested list

# lst1=[[1,2,3,4],[5,6,7,8]]
# lst2=lst1.copy()
# lst2[1][0]=100
# print(lst2)
#-------------------------------------------------------------------------------------------------------------------------------------------------

### deepcopy

# import copy
# lst1=[1,2,3,4]
# lst2=copy.deepcopy(lst1)
# print(lst2)
# lst2[1]=100
# print(lst2)
#-------------------------------------------------------------------------------------------------------------------------------------------------

### use of eval function
## how does eval work 
# 1.parse python expressiona 
# 2. compile into a byte code 
# 3. evaluate the python expressiona 
# 4. it will return the result

# var=compile("5*5","<string>","eval")
# print(eval(var))

# x=10
# print(eval("x+50+x**2",{"x":x}))

# x=100
# z=100
# print(eval("x+z+w",{"x":x,"z":100,"w":1000}))
#---------------------------------------------------------------------------------------------------------------------------------------------

### Exception handling

# try:
#     a=1
#     b="s"
#     c=a+b
# except NameError as ex1:
#     print("the user have not defined the variable")
# except Exception as ex:
#     print(ex)

# try:
#     a=int(input("enter the number: "))
#     b=int(input("enter the number: "))
#     c=a+b
#     d=a*b
#     e=a/b
# except NameError:
#     print("user have not define the variable")
# except ZeroDivisionError:
#     print("please give number > 0")
# except TypeError:
#     print("enter the datatype similar")
# except Exception as ex:
#     print(ex)
# else:
#     print(c)
#     print(d)
#     print(e)
# finally:
#     print("execution is done")
#----------------------------------------------------------------------------------------------------------------------------------------------

### exam form can be filled or not by age comparing using exception handling

# # class Error(Exception): # building own custom class for exception
# #     pass
# class dobException(Error): # building own custom class for exception
#     pass
# # class customgeneric(Error): # building own custom class for exception
# #     pass
# year=int(input("Enter the year of birth: "))
# age=2026-year
# try:
#     if age<=30 and age>20:
#         print("you are elligible to apply the exam")
#     else:
#         raise dobException
# except dobException:
#     print("the age is not within criteria")
#--------------------------------------------------------------------------------------------------------------------------------------------