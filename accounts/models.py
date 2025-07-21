from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.

class EmployeeModel(AbstractUser):
    employee_code = models.CharField(max_length=10, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.employee_code:
            self.employee_code = uuid.uuid4().hex[:10].upper()
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f"{self.username} ({self.employee_code})"
        
        