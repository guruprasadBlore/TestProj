from __future__ import unicode_literals

from django.db import models



class Employee(models.Model):
    depts = (("TMS", "TMS"), ("Digital", "Digital"), ("BFSI", "BFSI"))
    name = models.CharField(max_length=120)
    department = models.CharField(choices=depts,max_length=50)

