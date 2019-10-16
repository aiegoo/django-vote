from django.db import models
from django.urls import reverse
# Create your models here.
class Bookmark(models.Model):
     site_name = models.CharField(max_length=100)
     url = models.URLField('site URL')
     url2 = models.URLField('site URL2')

     def __str__(self):
          return "💢 : "+self.site_name + ": " + self.url +" 주소2 ^_^ : "+ self.url2

     def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])