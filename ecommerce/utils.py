import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase+string.digits):
    rand_str = ''.join(random.choice(chars) for _ in range(size))
    print("rand string .........")
    print(rand_str)
    return rand_str

def unique_slug_generator(instance, new_slug):
    print('slug unique_slug_generator ....')
    if new_slug is not None:
        #slug = new_slug
        slug = new_slug.replace(" ", "-")
    else:
        slug    = slugify(instance.title)
    klass       = instance.__class__
    qs_exists   = klass.objects.filter( slug= slug).exists()
    if qs_exists:
        rand_str = random_string_generator(4)
        new_slug = f"{slug}-{rand_str}"
        return  unique_slug_generator(instance, new_slug)
    return slug
