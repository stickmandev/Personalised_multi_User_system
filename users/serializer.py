from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['logo', 'bussinessName', 'user'] 
        #fields = '__all__'        #to enable all fields