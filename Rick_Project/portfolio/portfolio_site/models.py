from django.core.exceptions import ValidationError
from django.db import models

# Custom validator function
def validate_min_length(value):
    min_length = 100
    if len(value) < min_length:
        raise ValidationError(f'Message must be at least {min_length} characters long.')

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(validators=[validate_min_length])

    def __str__(self):
        return f"Message from {self.name}"
