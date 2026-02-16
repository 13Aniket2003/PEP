from rest_framework import serializers
from .models import SignupUser

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignupUser
        fields=['id','username','email','password']