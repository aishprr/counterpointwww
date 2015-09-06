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


class Event(models.Model):

    name = models.CharField(max_length=128)
    where = models.CharField(max_length=128)
    when = models.DateTimeField(blank=True, null=True)
    ticketlink = models.CharField(max_length=128, blank=True, null=True) #put in images from bootstrap showing ticket and fblink
    fblink = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)


    def __unicode__(self):
        return self.name

    