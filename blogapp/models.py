from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')



class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    BLOG_CATEGORY_CHOICES = (('general','General'),('tech','Tech'),('food','Food'),('travel','Travel'),('sports','Sports'))
    TRENDING_CHOICES = (('trending', 'Trending'),('general','General'))

    blog_category = models.CharField(max_length=50, choices=BLOG_CATEGORY_CHOICES, default='general')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    trending = models.CharField(max_length=50, choices=TRENDING_CHOICES, default='general')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField()
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, 
                             self.slug])

    def fullname(self):
        return f'{self.author.first_name} {self.author.last_name}'

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Mention(models.Model):
    id= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username