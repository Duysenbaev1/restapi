from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField('Biography')
    image = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')

    def __str__(self):
    	return f'{self.username}'

class Project(models.Model):
    title = models.CharField('Title', max_length=256)
    description = models.TextField('Description')
    start_date = models.DateTimeField('Start time', auto_now_add=True)
    end_date = models.DateTimeField('End time')
    members = models.ManyToManyField(CustomUser, related_name='projects_as_member')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects_as_owner')

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField('Title', max_length=256)
    description = models.TextField('Description')
    deadline_date = models.CharField('Deadline Date', max_length=256, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
