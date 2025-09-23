import os
import django
import cloudinary
import cloudinary.api
from cloudinary.utils import cloudinary_url

# Sätt Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mindful_rise.settings")
django.setup()

from blog.models import Post, Category

# Konfigurera Cloudinary (se till att dina miljövariabler är rätt)
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
)

# Lista alla resurser från Cloudinary
resources = cloudinary.api.resources(max_results=100)  # max_results kan ändras

for r in resources.get('resources', []):
    # Exempel: ta filväg och dela upp i kategori/filer
    # Om filvägen är "media/django-summernote/2024-08-27/img.png"
    folder = r.get('folder', 'Uncategorized')  # folder används som kategori
    title = r.get('public_id').split('/')[-1]  # filnamn som titel
    url = r.get('secure_url')  # bild-URL

    # Hitta eller skapa kategori
    cat, created = Category.objects.get_or_create(name=folder)

    # Skapa blogginlägg
    post = Post.objects.create(
        title=title,
        category=cat,
        content=f'<p>Återskapat från Cloudinary: <img src="{url}" alt="{title}"></p>',
        # Om du har ett separat fält för bild:
        # image_url=url
    )

    print(f"Skapade post: {title} i kategori {cat.name}")
