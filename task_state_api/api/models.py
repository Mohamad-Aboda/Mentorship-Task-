from django.db import models
from django.db.models.enums import Choices

class Task(models.Model):
    CHOICES = (
        ('draft', 'Draft'), 
        ('active', 'Active'), 
        ('done', 'Done'), 
        ('archived', 'Archived'),
    )
    title = models.TextField()
    state = models.CharField(max_length = 9, choices=CHOICES, default='draft')


    def __str__(self):
        return self.title 