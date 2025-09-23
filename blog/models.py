import os
import django

# Ställ in Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mindful_rise.settings')
django.setup()

from blog.models import Post, Category
from django.contrib.auth.models import User

# Ange användaren som ska vara författare
author = User.objects.get(username='christina')

# Lista över alla kategorier som du vill återskapa
categories_data = [
    'media/django-summernote/2024-08-27',
    'media/django-summernote/2024-08-09',
    'media/django-summernote/2024-08-08',
    'static/img_readme',
    'static/images',
    'static/staticfiles/images',
    'static/summernote',
    'samples',
    'samples/landscapes',
    'samples/animals',
    'samples/food',
    'samples/ecommerce',
    'samples/people',
    'Cloudinary'
]

# Skapa eller hämta kategorier
categories_dict = {}
for cat_name in categories_data:
    category, created = Category.objects.get_or_create(name=cat_name)
    categories_dict[cat_name] = category

# Lista över blogginlägg med titel, slug och Cloudinary-URL
posts_data = [
    {
        "title": "img2carousel_y9ckwt",
        "slug": "img2carousel_y9ckwt",
        "image_url": "https://res.cloudinary.com/dvh69l0yv/image/upload/v1725215184/img2carousel_y9ckwt",
        "categories": ["media/django-summernote/2024-08-27"]
    },
    {
        "title": "fxz5rknmf5jmnihzxk2h",
        "slug": "fxz5rknmf5jmnihzxk2h",
        "image_url": "https://res.cloudinary.com/dvh69l0yv/image/upload/v1725198212/fxz5rknmf5jmnihzxk2h",
        "categories": ["static/img_readme"]
    },
    {
        "title": "q7okk3ff8ucqqokazqvs",
        "slug": "q7okk3ff8ucqqokazqvs",
        "image_url": "https://res.cloudinary.com/dvh69l0yv/image/upload/v1725198196/q7okk3ff8ucqqokazqvs",
        "categories": ["samples"]
    },
    {
        "title": "nss9effo3jq1shb1cakp",
        "slug": "nss9effo3jq1shb1cakp",
        "image_url": "https://res.cloudinary.com/dvh69l0yv/image/upload/v1725197946/nss9effo3jq1shb1cakp",
        "categories": ["samples/landscapes"]
    },
    {
        "title": "e8iqem9lo1eicqsa9p8l",
        "slug": "e8iqem9lo1eicqsa9p8l",
        "image_url": "https://res.cloudinary.com/dvh69l0yv/image/upload/v1725093790/e8iqem9lo1eicqsa9p8l",
        "categories": ["samples/animals"]
    },
    {
        "title": "bvzaeipqipbl2ithbmuk",
        "slug": "bvzaeipqipbl2ithbmuk",
        "image_url": "https://res.cloudinary.com/dvh69l0yv/image/upload/v1725093413/bvzaeipqipbl2ithbmuk",
        "categories": ["samples/food"]
    }
]

# Skapa inlägg och koppla kategorier
for pdata in posts_data:
    post = Post.objects.create(
        title=pdata['title'],
        author=author,
        content="Återskapat från Cloudinary",
        slug=pdata['slug']
    )
    # Lägg till Cloudinary-bilden
    if pdata.get('image_url'):
        post.featured_image = pdata['image_url']
        post.save()
    
    # Lägg till kategorier
    for cat_name in pdata['categories']:
        post.categories.add(categories_dict[cat_name])
    
    print(f"Skapade inlägg: {post.title} med kategorier {[c.name for c in post.categories.all()]}")
