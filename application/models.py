from django.db import models


class Member(models.Model):
    
    andrewid = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    part = models.CharField(max_length=128)
    major = models.CharField(max_length=128)
    graduation = models.IntegerField(default=0)
    bio = models.CharField(max_length=2000)
    alumni = models.BooleanField(default=False)
    post = models.CharField(max_length=128)

    def __unicode__(self):
        return self.andrewid


#class Event(models.Model):

