from django.contrib import admin
from .models import ImageModel ,Subscription  ,Membership,UserMembership
# Register your models here. 
admin.site.register(ImageModel)
admin.site.register(Subscription)
admin.site.register(Membership)
admin.site.register(UserMembership)