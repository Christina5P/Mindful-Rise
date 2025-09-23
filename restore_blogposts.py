import os
import django
import cloudinary
import cloudinary.api

# --- Setup Django ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mindful_rise.settings')
django.setup()

# --- Importera modeller ---
from blog.models import Post, Category
from django.contrib.auth.models import User

# --- Konfigurera Cloudinary direkt med din URL ---
cloudinary.config(
    cloudinary_url="cloudinary://618768418781469:Q8KVKcOdIzeC4kCaKocmseNCHmM@dvh69l0yv"
)

# --- Hämta första användaren som author ---
author = User.objects.first()
if not author:
    print("Ingen User i databasen, skapa en först!")
    exit()

# --- Funktion för att skapa Post ---
def create_post(title, url, author):
    slug = title.lower().replace(" ", "-")
    if not Post.objects.filter(title=title).exists():
        post = Post.objects.create(
            title=title,
            content="Återställd från Cloudinary",
            featured_image=url,
            author=author,
            slug=slug,
            status=1,  # Published
        )
        print(f"Skapat: {title}")
    else:
        print(f"Finns redan: {title}")

# --- Hämta alla Cloudinary-resurser med paginering ---
next_cursor = None
while True:
    try:
        resources = cloudinary.api.resources(
            type="upload",
            max_results=100,
            next_cursor=next_cursor
        )
    except Exception as e:
        print("Fel vid hämtning från Cloudinary:", e)
        break

    for res in resources.get('resources', []):
        title = res['public_id'].split('/')[-1]
        url = res['secure_url']

        # Skapa Post
        create_post(title, url, author)

        # Skapa kategori baserat på mapp i Cloudinary (om finns)
        folder = '/'.join(res['public_id'].split('/')[:-1])
        if folder:
            category, created = Category.objects.get_or_create(
                name=folder,
                defaults={'slug': folder.lower().replace(" ", "-")}
            )
            post = Post.objects.get(title=title)
            post.categories.add(category)

    next_cursor = resources.get('next_cursor')
    if not next_cursor:
        break

print("Klart! Alla Cloudinary-bilder har nu blogposter och kategorier.")
