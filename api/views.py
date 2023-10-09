from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response

from app.models import *
from .serializers import UserSerializer, TaskSerializer, ProjectSerializer
from .permissions import UserPermission, UserDetailPermission, TaskPermission, ProjectPermission


# USER
@api_view(['GET', 'POST'])
@permission_classes([UserPermission])
def user(request):
	if request.method == 'GET':
		member = CustomUser.objects.all()
		serializers = UserSerializer(member, many=True, context = {'request':request})
		return Response(serializers.data, status=HTTP_200_OK)
	elif request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@permission_classes([UserDetailPermission])
def user_detail(request, pk):
    try:
        member = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(member, data=request.data, partial=True,context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        member = CustomUser.objects.all()
        serializers = UserSerializer(member, many=True, context = {'request':request})
        return Response(serializers.data, status=HTTP_200_OK)

    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# PROJECT
@api_view(['GET', 'POST'])
@permission_classes([ProjectPermission])
def project(request):
	if request.method == 'GET':
		project = Project.objects.all()
		serializers = ProjectSerializer(project, many=True)
		return Response(serializers.data, status=HTTP_200_OK)
	elif request.method == 'POST':
		serializer = ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@permission_classes([ProjectPermission])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        project = Project.objects.all()
        serializers = ProjectSerializer(project, many=True)
        return Response(serializers.data, status=HTTP_200_OK)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TASK
@api_view(['GET', 'POST'])
@permission_classes([TaskPermission])
def task(request):
	if request.method == 'GET':
		task = Task.objects.all()
		serializers = TaskSerializer(task, many=True)
		return Response(serializers.data, status=HTTP_200_OK)
	elif request.method == 'POST':
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
@permission_classes([TaskPermission])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        task = Task.objects.all()
        serializers = TaskSerializer(task, many=True)
        return Response(serializers.data, status=HTTP_200_OK)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)