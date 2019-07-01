from django.db import models

class Course(models.Model):
    subject = models.CharField(max_length=200)
    def __str__(self):
        return self.subject

class Carrier(models.Model):
    carrier_post = models.CharField(max_length=200)
    carrier_subjct = models.CharField(max_length=200)
    required = models.IntegerField(default=0)
    def __str__(self):
        return self.carrier_post

class Event(models.Model):
    event = models.CharField(max_length=200)
    fr = models.DateTimeField("from")
    to = models.DateTimeField()
    total = models.IntegerField(default=0)

class Exam(models.Model):
    Exam_for = models.CharField(max_length=200)
    date = models.DateTimeField()
