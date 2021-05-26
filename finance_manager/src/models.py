from django.db import models


class SomeUser(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()


class Income(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    user_id = models.IntegerField(blank=False)
    amount = models.FloatField()
    date = models.DateField()


class Outcome(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    user_id = models.IntegerField(blank=False)
    amount = models.FloatField()
    date = models.DateField()
