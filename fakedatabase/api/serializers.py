from django.urls import path, include
from django.contrib.auth.models import Person
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'job', 'address', 'email', 'address' ]