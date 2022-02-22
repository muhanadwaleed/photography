from django.contrib import admin
from Barghash.models import *


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    ordering = ['-date']

class MessagesAdmin(admin.ModelAdmin):
    readonly_fields = ['name','subject','message','contact_way']


admin.site.register(Profile)
admin.site.register(ContactUs)
admin.site.register(Messages,MessagesAdmin)
admin.site.register(Instagram)
admin.site.register(AboutPage)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
