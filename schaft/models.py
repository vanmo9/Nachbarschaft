from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images/')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self):
        return self.title 

class Profile(models.Model):
    User.pro_user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')
    email = models.EmailField(max_length=30)
    neighborhood = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  

class Location(models.Model):
    location_name = models.CharField(max_length = 30)
    hood = models.CharField(max_length = 30)


    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()  

class NachbarSchaft (models.Model):
    nach_user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    User.location = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.hood_name  

class Business(models.Model):
    business_name = models.CharField(max_length=30, blank=True)
    User.bus_user = models.ForeignKey(User, on_delete = models.CASCADE)
    nachbarschaft_id = models.ForeignKey(User, on_delete = models.CASCADE)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.business_name        
                                
