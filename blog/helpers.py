
from django.utils.text import slugify





import string
import random
def random_string(N):
     res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
     return res
# print result
# print("The generated random string : " + str(res))




def generate_slug(text):
    new_slug=slugify(text)
    from blog.models import Post
    if Post.objects.filter(slug=new_slug).exists():
       return generate_slug(text + random_string(5))
    return new_slug    