from django.db import models
#from django.db import models

from django.db import models

class Conference(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    research_paper = models.FileField(upload_to='research_papers/', blank=True, null=True)
    review = models.TextField(blank=True, null=True)


class Chair(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password=models.TextField()
    # Add other fields as needed for Chair

class Reviewer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password=models.TextField()

    # Add other fields as needed for Reviewer

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password=models.TextField()

    # Add other fields as needed for User
