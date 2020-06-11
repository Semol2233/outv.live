from django.db import models
from datetime import datetime

class cetagry(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name

class author (models.Model):
    author_name = models.CharField(max_length=30)

    def __str__(self):
        return self.author_name


class post(models.Model):
    authors       = models.ForeignKey(author,on_delete=models.CASCADE)
    catagry       = models.ForeignKey(cetagry,on_delete=models.CASCADE)
    title         = models.CharField(max_length=100)
    details       = models.TextField(blank=True)
    post_img      = models.ImageField(upload_to='img/')
    post_view     = models.IntegerField(blank=True,default=0)
    release_date  = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.title
    

class livtv(models.Model):
    live_tv_url = models.URLField(max_length=500,blank=False)
    live_logo   = models.ImageField(upload_to='live_tv_logo/' ,blank=False)