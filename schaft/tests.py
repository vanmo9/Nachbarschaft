from django.test import TestCase
from .models import Profile,Post,tag,Location,NachbarSchaft,Business
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.vanmo9 = Profile(profile_name = 'vanmo9',username='vanmo9',email='vanmowha@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.vanmo9,Profile))

    def test_save(self):
        self.vanmo9.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)


class PostTestClass(TestCase):
    def setUp(self):
        self.vanmo9 = Profile(image_name = 'vanmo9',username='vanmo9',email='vanmowha@gmail.com')
        self.vanmo9.save_profile()

        self.new_tag=tag(tag='testing')
        self.new_tag.save()

        self.new_post =Posts(caption="Woooow!!!!",profile=self.vanmo9)
        self.new_post.save()

        self.new_post.tag.add(self.new_tag)

    def tearDown(self):
        Profile.objects.all().delete()
        tag.objects.all().delete()
        Posts.objects.all().delete()    

    def test_posts(self):
        posts = Posts.posts()
        self.assertTrue(len(posts)>0) 


class Location(TestCase):
    def setUp(self):
        self.new_location = Location(location_name = 'Oslo')
        self.new_location.save_location()
        self.new_category = Category(category_name = 'Fashion')
        self.new_category.save_category()

    def nachbarSchaft(self):
        self.assertTrue(isinstance(self.new_photo,Photo))
        self.assertTrue(isinstance(self.new_location,Location))
        self.assertTrue(isinstance(self.new_category,Category))

    def business(self):
        self.new_image.save_image()
        instance = Business.objects.get(business_name='Fashion')
        self.assertTrue(instance.category_name=='Fashion')



    def location(self):
        self.new_image.save_image()
        instance = Location.objects.get(location_name='Oslo')
        self.assertTrue(instance.location_name=='Oslo')
