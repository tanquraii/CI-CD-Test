from movies.models import CatUser
from rest_framework import serializers

class CatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatUser
        fields = ['id','nickname']

class CatUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatUser
        fields = '__all__'