from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

import datetime

class prospect(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0} {1} {2}".format(
            self, self.firstname, self.lastname, self.email)

# Create your models here.
