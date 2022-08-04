from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from  .helpers import *
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    slug=models.SlugField(max_length=330, null=True,blank=True)
    views=models.IntegerField(default=0)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp=models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title +'by '+ self.author
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Post, self).save(*args, **kwargs)
    
    
    
class Blogcomment(models.Model):
    sno=models.AutoField(primary_key=True)   
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment + '...'+ 'by' + self.user.first_name
    