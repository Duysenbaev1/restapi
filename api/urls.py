from django.urls import path, include
from .views import user, user_detail, project, project_detail, task, task_detail


urlpatterns = [
	path('user/', user),
	path('user/<int:pk>/', user_detail),
	path('project/', project),
	path('project/<int:pk>/', project_detail),
	path('task/', task),
	path('task/<int:pk>/', task_detail),

	path('auth/', include('dj_rest_auth.urls'))

]

# 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