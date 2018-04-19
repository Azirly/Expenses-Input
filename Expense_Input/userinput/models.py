from django.db import models


class Expense(models.Model):
    date = models.DateTimeField('date published')
    value = models.IntegerField(default=0) *0.2
    reason = models.CharField(max_length=500)