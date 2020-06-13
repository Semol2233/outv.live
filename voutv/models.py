from django.db import models
from datetime import datetime







class Notice_bord(models.Model):
    Notice_name = models.CharField(max_length=200)
    details        = models.TextField(blank=True)
    img_Notice   = models.ImageField(upload_to='notice img/' ,blank=False)

    def __str__(self):
        return self.Notice_name

class photo (models.Model):
    img_title = models.CharField(max_length=30)
    img   = models.ImageField(upload_to='img/' ,blank=False)


    def __str__(self):
        return self.img_title


class  Academic_Info(models.Model):
    title          = models.CharField(max_length=100)
    slug           = models.CharField(max_length=250, blank=False,unique=True)
    details        = models.TextField(blank=True)
    img            = models.ImageField(upload_to='Academic_Info/' ,blank=False)


    def __str__(self):
        return self.title
    
class livtv(models.Model):
    live_tv_url = models.URLField(max_length=500,blank=False)
    live_logo   = models.ImageField(upload_to='live_tv_logo/' ,blank=False)
    channel_name = models.CharField(max_length=120)



class coverimg(models.Model):
    coverimg     = models.ImageField(upload_to='coverimg/')
    img_title    = models.CharField(max_length=200) 


# class class_video(models.Model):
#     coverimg     = models.ImageField(upload_to='coverimg/')
#     img_title    = models.CharField(max_length=200) 


class class_note(models.Model):
    title          = models.CharField(max_length=100)
    slug           = models.CharField(max_length=250, blank=False,unique=True)
    details        = models.TextField(blank=True)
    document       = models.FileField(upload_to='documents/')









# class post(models.Model):
#     authors        = models.ForeignKey(author,on_delete=models.CASCADE,related_name='items')
#     catagry        = models.ForeignKey(cetagry,on_delete=models.CASCADE)
#     title          = models.CharField(max_length=100)
#     slug           = models.CharField(max_length=250, blank=False,unique=True)
#     details        = models.TextField(blank=True)
#     post_img       = models.ImageField(upload_to='img/')
#     post_view      = models.IntegerField(blank=True,default=0)
#     release_date   = models.DateField(auto_now_add = True)
#     front_end_date = models.CharField(max_length=30,blank=False) 
    
#     def __str__(self):
#         return self.title