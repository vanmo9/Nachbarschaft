from django.contrib import admin
from .models import *  

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile) 
admin.site.register(Location)
admin.site.register(NachbarSchaft)
admin.site.register(Business)

