from django.contrib import admin

# Register your models here.
from .models import post,author,livtv,cetagry
admin.site.register(post)
admin.site.register(author)
admin.site.register(livtv)
admin.site.register(cetagry)





