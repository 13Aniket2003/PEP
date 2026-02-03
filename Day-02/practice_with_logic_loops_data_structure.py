### fibbonacci series till input without loop

# def fibonacci(n):
#     return n+(n-1)

# n=int(input())
# print(fibonacci(n))
#--------------------------------------------------------------------------------------------#
### fibbonacci series till input with loop

# def fib(x):
#     fib_series=[]
#     a,b=0,1

#     for i in range(x):
#         fib_series.append(a)
#         a,b=b,a+b
#     return fib_series

# n=int(input())
# print(fib(n))
#-------------------------------------------------------------------------------------------------------#
### fibbonacci series till input with recursion

# def fib(x):
#     if x==0:
#         return 0
#     if x==1:
#         return 1
#     return fib(x-1)+fib(x-2)

# n=int(input())
# for i in range(n):
#     print(fib(i))
#------------------------------------------------------------------------------------------------------------#
### swap upper case to lower or vice versa

# def swap_case(s):
#     a=s.swapcase()
#     return a
# if __name__ == "__main__" :
#     change=input()
#     print(swap_case(change))
#-------------------------------------------------------------------------------------------------------------------#
### in a sentance whereever there is any space it will covert to '-'

# def split_and_join(line):
#     sp=line.split()
#     print(sp)
#     j="-".join(sp)
#     return j

# if __name__ == "__main__":
#     line=input()
#     result=split_and_join(line)
#     print(result)
#--------------------------------------------------------------------------------------------------------------------------#
### create a list and using loop print each of element length till the length

# student=['Murthy','Bhanu','Aniket']
# for i in range(len(student)):
#     print(i, " is " ,student[i]," who have name length of ",len(student[i]))
#----------------------------------------------------------------------------------------------------------------------------#
### same above question ( using "enumerate" to replace range(len(a_list)))

# student=['Murthy','Bhanu','Aniket']
# for i,value in enumerate(student):
#     print(i,value)
#----------------------------------------------------------------------------------------------------------------------------#
### create a list and using loop print each of element length till the length and changing its index numbers
# student=['Murthy','Bhanu','Aniket']
# index=[11,12,13]
# for i in range(len(student)):
#     print(index[i], " is " ,student[i]," who have name length of ",len(student[i]))
#----------------------------------------------------------------------------------------------------------------------------#
### create a dictionary which stores 5 name and 5 rolls and print any values and any keys

# student={"Murthy":"45","Bhanu":"41","Aniket":44,"murthy":"25","bhanu":"12"}
# for i in student:
#     print(i, ":",student[i])
# print(" ")
# for key in student:
#     print(key)
# print(" ")
# for value in student.values():
#     print(value)

# student={"name":["Aniket","Murthy","Bhanu","murthy","bhanu"], "roll_no":[14,85,23,74,66]}
# for key in student:
#     print(key)
# print(" ")
# for value in student.values():
#     print(value)
#----------------------------------------------------------------------------------------------------------------------------#
### print name in upper or lower or find any character inside the name 

# name='Pillavullakandi Thekkeparambil Usha'
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.find('a'))
#---------------------------------------------------------------------------------------------------------------------------------------

### using f-string print happy new year and happy birthday if both dates are same print both and take input from user and if not same print today's date

# def special_days(newy,hbb,time):
#     if((newy=="01/01" or newy=="01-01" or newy=="1/1" or newy=="1-1" or newy=="1 1" or newy=="01 01") and (time=="00:00" or time=="12:00 AM" or time=="12:00 am")):
#         print("Happy new year")
#     if(hbb=="13/04/1998" or hbb=="13-04-1998" or hbb=="13-4-1998" or hbb=="13/4/1998"):
#         print("Happy Birthday")
#     else:
#         return("Regular day")

# if __name__ == "__main__":
#     x=input()
#     y=input()
#     z=input()
#     a=special_days(x,y,z)
#     print(a)
#----------------------------------------------------------------------------------------------------------------------------#

### add element to list

# name=["Aniket","Bhanu","Murthy"]
# name.append("Sadgyan")
# print(name)
#----------------------------------------------------------------------------------------------------------------------------#

### replace element of a list with new value 

#name=["Aniket","Bhanu","Murthy","Sadgyan"]
# name.append("Sadgyan")
# name[0]="Nana"
# print(name)

# a = name.__contains__("Aniket") ### checking whether the value exist or not
# print(a)

# b=enumerate(name) ### memory address of the index
# print(b)

# a=list((i-len(name),n)
#      for i,n in enumerate (name))  ##### enumerate is used to replace range or to get get index and the value both
# print(a)
# a=name[:3]
# print(a)

# name2=name[2:4]
# a=id(name2) ### shallow copy that is making a subset or the whole set
# print(name2)
# print(a)
# b= name[0] is name2[0] ### checking whether truely eleminating the element which have not added in subset
# print(b)

# a=[1,2,3,4,5,6,7,8,9,0]
# b=a[::-2] ### striding that is jumping number how much gap should be there
# print(b)
#----------------------------------------------------------------------------------------------------------------------------#

### literals and constructors

# types={'name':str,'age':int,'address':str}
# types2=dict(name=str,age=int,address=str)
# print(types['age'])

# types['language']=str
# print(types)
#----------------------------------------------------------------------------------------------------------------------------#

### create a dictionary of inventory which has the name of movie, cast,and total revenue generation and print all value and print any value with proper sentance

# movies={"name":["KGF","KGF2","Pushpa","Pushpa2","Bahubali","Bahubali2"],
#         "cast":["Yash","Yash","Allu Arjun","Allu Arjun","Prabhas","Prabhas"],
#         "revenue_generated":["400 cr","1200 cr","800 cr","1700 cr","500 cr","1800 cr"]}
# Name= input("enter movie name: ")
# if(Name in movies["name"]):
#     i=movies["name"].index(Name)
#     print(f"The movie {movies['name'][i]} stars {movies['cast'][i]} and earned {movies['revenue_generated'][i]}.")
# else:
#     print("movie not found")
#----------------------------------------------------------------------------------------------------------------------------#