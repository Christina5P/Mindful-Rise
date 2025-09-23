#!/usr/bin/env python
import os
import django

# 1️⃣ Ange Django settings innan vi importerar modeller
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mindful_rise.settings')
django.setup()  # Körs endast en gång här

# 2️⃣ Importera modeller EFTER django.setup()
from blog.models import Post, Category
from django.contrib.auth.models import User

# 3️⃣ Exempel på återställning av blogginlägg
def restore_posts():
    # Hitta en användare som ska äga inläggen
    author = User.objects.first()
    if not author:
        print("Ingen användare finns. Skapa en först.")
        return

    # Skapa exempel-kategori om den inte finns
    cat, created = Category.objects.get_or_create(name="Restored")
    if created:
        print(f"Kategori '{cat.name}' skapad.")

    # Skapa ett testinlägg
    post, created = Post.objects.get_or_create(
        title="Återskapat inlägg",
        defaults={
            "author": author,
            "content": "Detta inlägg återskapades från backup.",
            "slug": "aterskapat-inlagg",
        },
    )

    # Lägg till kategori
    post.categories.add(cat)
    post.save()

    print(f"Inlägg '{post.title}' återskapat med kategori '{cat.name}'.")

# 4️⃣ Kör funktionen
if __name__ == "__main__":
    restore_posts()
