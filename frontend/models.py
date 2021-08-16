from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Portfolio(models.Model):
    port_img1 = models.ImageField(blank=True, verbose_name='Profile Image1', null=True, upload_to='uploads/', default='')
    port_title1 = models.CharField(max_length=100, verbose_name='Profile Title1')
    port_img2 = models.ImageField(blank=True, verbose_name='Profile Image2', null=True, upload_to='uploads/', default='')
    port_title2 = models.CharField(max_length=100, verbose_name='Profile Title2')
    
    port_img3 = models.ImageField(blank=True, verbose_name='Profile Image3', null=True, upload_to='uploads/', default='')
    port_title3 = models.CharField(max_length=100, verbose_name='Profile Title3')
    port_img4 = models.ImageField(blank=True, verbose_name='Profile Image4', null=True, upload_to='uploads/', default='')
    port_title4 = models.CharField(max_length=100, verbose_name='Profile Title4')
    port_img5 = models.ImageField(blank=True, verbose_name='Profile Image5', null=True, upload_to='uploads/', default='')
    port_title5 = models.CharField(max_length=100, verbose_name='Profile Title5')
    port_img6 = models.ImageField(blank=True, verbose_name='Profile Image6', null=True, upload_to='uploads/', default='')
    port_title6 = models.CharField(max_length=100, verbose_name='Profile Title6')
    port_img7 = models.ImageField(blank=True, verbose_name='Profile Image7', null=True, upload_to='uploads/', default='')
    port_title7 = models.CharField(max_length=100, verbose_name='Profile Title7')
    port_img8 = models.ImageField(blank=True, verbose_name='Profile Image8', null=True, upload_to='uploads/', default='')
    port_title8 = models.CharField(max_length=100, verbose_name='Profile Title8')
    port_img9 = models.ImageField(blank=True, verbose_name='Profile Image9', null=True, upload_to='uploads/', default='')
    port_title9 = models.CharField(max_length=100, verbose_name='Profile Title9')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    class Meta():
        verbose_name_plural = 'Portfolio'


    def __str__(self):
        return self.port_title1

    def my_img1(self):
        if self.port_img1:
            return self.port_img1.url
    def my_img2(self):
        if self.port_img2:
            return self.port_img2.url
    def my_img3(self):
        if self.port_img3:
            return self.port_img3.url
    def my_img4(self):
        if self.port_img4:
            return self.port_img4.url
    def my_img5(self):
        if self.port_img5:
            return self.port_img5.url
    def my_img6(self):
        if self.port_img6:
            return self.port_img6.url
    def my_img7(self):
        if self.port_img7:
            return self.port_img7.url
    def my_img8(self):
        if self.port_img8:
            return self.port_img8.url
    def my_img9(self):
        if self.port_img9:
            return self.port_img9.url
    

class Post(models.Model):
    
    RECENT_PIC = "R"
    PORTFOLIO_PIC = "P"
    ACTIVITY = "A"
    BLOG_NEWS = "B"
    CHOOSE = ""

    NEWS_TYPE = [
        (RECENT_PIC, 'Recent_Pic'),
        (PORTFOLIO_PIC, 'Portfolio_Pic'),
        (ACTIVITY, 'Activity'),
        (BLOG_NEWS, 'Blog_News'),
        (CHOOSE, 'Please Choose')

    ]
    
    add_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/' )
    add_title = models.CharField(max_length=100, verbose_name='Profile Title')
    listing_type = models.CharField(max_length=40, verbose_name='Listing Type', null=True)
    add_desription = models.TextField(verbose_name='Description')
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    class Meta():
        verbose_name_plural = 'Post'


    def __str__(self):
        return self.add_title

    def my_img1(self):
        if self.add_img:
            return self.add_img.url

class Blog(models.Model):
    FEATURE = 'Feature'
    NO_FEATURE = 'No Feature'
    CHOOSE = ''

    APPEAR_HOME_FIELD=[
        (FEATURE, 'Appear on home'),
        (NO_FEATURE, "Don't show on home"),
        (CHOOSE, 'Please Choose')
    ]
    blog_img = models.ImageField(blank=True, verbose_name='blog Image', null=True, upload_to='uploads/', default='')
    blog_title = models.CharField(max_length=100, verbose_name='blog Title')
    blog_desription = models.TextField(verbose_name='Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appear_home = models.CharField(max_length=50, choices=APPEAR_HOME_FIELD, default=CHOOSE)
    
    class Meta():
        verbose_name_plural = 'blog'


    def __str__(self):
        return self.blog_title

    def my_img2(self):
        if self.blog_img:
            return self.blog_img.url


class Mudia (models.Model):
    pst_img = models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='uploads/', default='')
    pst_title = models.CharField(max_length=100, verbose_name='Title')
    
    
    class Meta():
        verbose_name_plural = 'Mudia'


    def __str__(self):
        return self.pst_title

    def my_img3(self):
        if self.pst_img:
            return self.pst_img.url


class About (models.Model):
    about_img = models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='uploads/', default='')
    about_title = models.CharField(max_length=100, verbose_name='Title')
    
    
    class Meta():
        verbose_name_plural = 'About'


    def __str__(self):
        return self.about_title

    def my_img4(self):
        if self.about_img:
            return self.about_img.url

class Addpic (models.Model):
    pc_img = models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='uploads/', default='')
    pc_title = models.CharField(max_length=100, verbose_name='Title')
    pc_desription = models.TextField(verbose_name='Description')
    
    class Meta():
        verbose_name_plural = 'Addpic'


    def __str__(self):
        return self.pc_title

    def my_img5(self):
        if self.pc_img:
            return self.pc_img.url

class Addpost (models.Model):
    addpost_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/', default='')
    addpost_desription = models.TextField(verbose_name='Description')
    
    
    class Meta():
        verbose_name_plural = 'Addpost'


    def __str__(self):
        return self.addpost_desription

    def my_img6(self):
        if self.addpost_img:
            return self.addpost_img.url

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)