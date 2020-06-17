from django.db import models
from datetime import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField




class Notice_bord(models.Model):
    title = models.CharField(max_length=200)
    details        =  RichTextUploadingField(blank=True )
    img          = models.ImageField(upload_to='notice img/' ,blank=False)
    release_date   = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title

class photo (models.Model):
    title = models.CharField(max_length=30)
    img   = models.ImageField(upload_to='img/' ,blank=False)
    release_date   = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.title


class  Academic_Info(models.Model):
    title          = models.CharField(max_length=100)
    slug           = models.CharField(max_length=250, blank=False,unique=True)
    details        = models.TextField(blank=True)
    img            = models.ImageField(upload_to='Academic_Info/' ,blank=False)
    release_date   = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.title
    
class livtv(models.Model):
    live_tv_url = models.URLField(max_length=500,blank=False)
    live_logo   = models.ImageField(upload_to='live_tv_logo/' ,blank=False)
    channel_name = models.CharField(max_length=120)
    release_date   = models.DateField(auto_now_add = True)



class coverimg(models.Model):
    coverimg     = models.ImageField(upload_to='coverimg/')
    img_title    = models.CharField(max_length=200) 
    release_date   = models.DateField(auto_now_add = True)    



class class_note(models.Model):
    title          = models.CharField(max_length=100)
    slug           = models.CharField(max_length=250, blank=False,unique=True)
    details        = models.TextField(blank=True)
    document       = models.FileField(upload_to='documents/')
    note_img       = models.ImageField(upload_to='note_img/')
    release_date   = models.DateField(auto_now_add = True)






class Apps_about(models.Model):
    about          = models.CharField(max_length=100)
    details        = models.TextField(blank=True)
    facebook_link  = models.URLField(max_length=500,blank=False)






class Apps_slider(models.Model):
    img            = models.ImageField(upload_to='apps_Academic_Info/' ,blank=False)
    release_date   = models.DateField(auto_now_add = True)


class Apps_linkup(models.Model):
    item  = models.CharField(max_length=20)
    link = models.URLField(max_length=500,blank=False)
    release_date   = models.DateField(auto_now_add = True)
















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




# home page


