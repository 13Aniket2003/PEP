# Using GET method -----------------

from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#------------------------------------------------------------------------



























# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer

# @api_view(['POST'])
# def create_student(request):
#     serializer = StudentSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {
#                 "message": "Student created successfully",
#                 "data": serializer.data
#             },
#             status=status.HTTP_201_CREATED
#         )

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)