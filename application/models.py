from django.db import models


class Member(models.Model):
    
    andrewid = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    part = models.CharField(max_length=128)
    major = models.CharField(max_length=128)
    graduation = models.IntegerField(default=0)
    bio = models.CharField(max_length=2000)
    alumni = models.BooleanField(initial=False)

    def __unicode__(self):
        return self.andrewid

