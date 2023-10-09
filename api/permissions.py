from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
	def has_permission(self, request, view):
		if request.method == 'GET':
			return True
		elif request.method in ['POST', 'PUT', 'DELETE']:
			return request.user.is_authenticated

class UserDetailPermission(BasePermission):
	def has_permission(self, request, view):
		if request.method in ['GET','PUT', 'DELETE']:
			return request.user.is_authenticated

class TaskPermission(BasePermission):
	def has_permission(self, request, view):
		if request.method in ['GET', 'PUT', 'POST', 'DELETE']:
			return request.user.is_authenticated

class ProjectPermission(BasePermission):
	def has_permission(self, request, view):
		if request.method == 'GET':
			return True
		elif request.method in ['POST', 'PUT', 'DELETE']:
			return request.user.is_authenticated