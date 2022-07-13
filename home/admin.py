from django.contrib import admin
from blog.models import Post
# Register your models here.
from home.models import Contact
admin.site.register(Contact)
admin.site.register(Post)