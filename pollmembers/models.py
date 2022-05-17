
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from datetime import date

borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

@property
def is_overdue(self):                                             
    if self.due_back and date.today() > self.due_back:
        return True
    return False

class BookInstance(models.Model):
    
    class Meta:
        
        permissions = (("can_mark_returned", "Set book as returned"),)


# Create your models here.

class Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    age = models.IntegerField(null=True, blank=True)
    profile_picture = models.TextField()
    active = models.BooleanField(default=True)
    cohort = models.ForeignKey("Cohort", on_delete=models.SET_NULL, null=True)

class Cohort(models.Model):
    name = models.CharField(max_length=50)



# Poll 
    # name (CharField)
    # 


# Poll_option
   # name (CharField)
   # image (text)
   # poll (ForeignKey)


# Poll_Answers
  # poll_option (ForeignKey)
  # answer (BooleanField)