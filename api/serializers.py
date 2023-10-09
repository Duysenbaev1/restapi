from rest_framework import serializers
from app.models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = [
		'id',
		'username',
		'password',
		'image',

		]

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'