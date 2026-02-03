# In the Gregorian calender, three conditions are used to identify leap years: 
# The year can be evenly divided by 4, is a leap year, unless:
# the year can be evenly divided by 100, it is not a leap year, unless:
# the year is also evenly divided by 400, then it is a leap year.
# This means that in the Georgorian calendar, the years 2000 and 2400 are leap years
# 1900,2100,2200,2300, and 2500 are not leap year

# def is_leap(year):
#     leap=False
#     if (year % 4==0 and year%100!=0) or (year%400==0):
#         leap=True
#     return leap
# year=int(input())
# print(is_leap(year))
#---------------------------------------------------------------------------------------------------------------------------------------------

# '''Question from Hackerank----> 
# There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.

# The new pile should follow these directions:

# * If cube[i] is on top of cube[j], then
# sideLength[i] ≥ sideLength[j]

# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.

# Print Yes if it is possible to stack the cubes following the above rules.
# Otherwise, print No.

# Example 1

# blocks = [1, 2, 3, 8, 7]

# Result: No

# After choosing the rightmost element 7, choose the leftmost element 1.
# After that, the choices are 2 and 8. These are both larger than the top block of size 1.

# Example 2

# blocks = [1, 2, 3, 7, 8]

# Result: Yes

# Choose blocks from right to left in order to successfully stack the blocks.

# Input Format

# The first line contains a single integer T, the number of test cases.

# For each test case, there are 2 lines:

# * The first line contains integer n, the number of cubes.
# * The second line contains n space separated integers, denoting the side lengths of each cube in that order.

# Constraints

# 1 ≤ T ≤ 5
# 1 ≤ n ≤ 10⁵
# 1 ≤ sideLength < 2³¹
# Output Format

# For each test case, output a single line containing either Yes or No.'''

# for _ in range(int(input())): #-----> use of _ is because we are not caring about the input range
#     n= int(input())
#     b = list(map(int, input().split()))
#     i = 0
#     while i < n - 1 and b[i] >= b[i+1]:
#         i += 1
#     while i < n - 1 and b[i] <= b[i+1]:
#         i += 1
#     print("Yes" if i == n - 1 else "No")

# after compile outputs---> 
# 2
# 6
# 4 3 2 1 3 4
# Yes
# 3
# 1 3 2
# No
#---------------------------------------------------------------------------------------------------------------------------------------------

##### create an project and App in django and link the url of the app with the project and make 2 pages to see in browser

## Urls for project
# from django.contrib import admin
# from django.urls import include,path
# from . import views

# urlpatterns = [
#     path("impossible1/",include("impossible1.urls")),
#     path("impossible2/",include("impossible2.urls")),
#     path('', views.index, name = 'index'),
#     path('admin/', admin.site.urls),
#     path('car/',views.car,name='car'),
#     path('bike/',views.bike,name='bike'),
#     path('auto/',views.auto,name='auto'),
# ]
#------------------------------------------------------------

## Views of project

# from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return render(request,'index.html')

# def car(request):
#     return HttpResponse("This is fastest car")

# def bike(request):
#     return HttpResponse("This is bike")

# def auto(request):
#     return HttpResponse("this is auto")
#-----------------------------------------------------------------

## Views of app

# from django.shortcuts import render
# from django.http import HttpResponse
# def four_wheel(respons):
#     return HttpResponse("out of wheel")
#---------------------------------------------------------------

# Urls of app

# from django.urls import path
# from . import views
# urlpatterns = [
#     path("four_wheel",views.four_wheel,name="four_wheel"),
# ]
#--------------------------------------------------------------------

### Make a file index.html and layout.html inside folder template in project 

# {% load static %}
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     {% block head %}
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Indexing</title>
#     <link rel="stylesheet" href="{% static 'style.css'%}">
#     {% endblock head%}
# </head>
# <body>
#     {% block h1 %}
#     This is out home page
#     {% endblock h1 %}
# </body>
# </html>
#--------------------------------------------------------------------------

## written html in layout.html and use load static to load the css file and also used " %block file_type {Like,head or titile ex---> %block title} %"
## the command of block is {% block head %} content {% endblock head %}-----> we use block command to write the html code in block wise such 
## that in future when large code or large file or a part wise design will be done that time there will be no issue to change any block directly 
## and it will be easy to use too.

# {% extends "layout.html"%}

## to link or access the layout.html in index.html or to copy or to use it as index.html we use "% extends "file_name" % "
## ---> we use it to access or link the file to another void file.
#----------------------------------------------------------------------------------------------------------------------------------------------------
