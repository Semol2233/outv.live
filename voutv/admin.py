from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header = 'Admin - Boutv'


class Notice_bordAdmin(admin.ModelAdmin):
    list_display = ('title','release_date')
    list_filter       = ('release_date',)














admin.site.register(Notice_bord ,Notice_bordAdmin)
admin.site.register(photo)
admin.site.register(Academic_Info)
admin.site.register(coverimg)
admin.site.register(livtv)
admin.site.register(class_note)


admin.site.register(Apps_about)
admin.site.register(Apps_slider)
admin.site.register(Apps_linkup)








