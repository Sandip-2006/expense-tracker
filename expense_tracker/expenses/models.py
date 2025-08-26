from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Bills', 'Bills'),
        ('Others', 'Others'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(default=timezone.now, blank=True, null=True)  # ✅ manual ya default

    def __str__(self) -> str:
        return f"{self.description} - {self.amount}"
