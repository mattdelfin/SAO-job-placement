from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class OJTHiring(models.Model):
    pass

class OJTRequirements(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE) # Change to Students Model
    non_disclosure = models.BooleanField(default=False)
    biodata = models.BooleanField(default=False)
    parents_consent = models.BooleanField(default=False)
    application_letter = models.BooleanField(default=False)
    medical = models.BooleanField(default=False)
    moa = models.BooleanField(default=False)
    endorsement = models.BooleanField(default=False)

    def __str__(self):
        return self.student.email

class Seminar(models.Model):
    title = models.CharField(max_length=100, null=False, default="")
    theme = models.CharField(max_length=150, null=False, default="")
    date_of_event = models.DateField(null=False, default="")

    def __str__(self):
        return self.title
    
class CareerGuidanceTracker(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE) # Change to studentModel
    seminar = models.ForeignKey(Seminar, null=True, on_delete=models.SET_NULL)
    attended = models.BooleanField(default=False)

