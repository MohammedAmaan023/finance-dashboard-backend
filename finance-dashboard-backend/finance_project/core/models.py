from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('viewer', 'Viewer'),
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Record(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=50)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"