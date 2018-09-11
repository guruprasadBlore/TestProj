from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from ecommerce.models import post
# Create your models here.

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    post = models.ForeignKey(post)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

