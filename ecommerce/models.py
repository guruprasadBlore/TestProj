from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now_add=True,auto_now=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='post_likes')

    class Meta:
        permissions = (("Can_Modify","Can Modify the blog content"),)
        ordering = ('-updated',)

    def save(self,*args,**kwargs):
        if self.id is None:
            self.slug = slugify(self.title)
        super(post,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.title)
