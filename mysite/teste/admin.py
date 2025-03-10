from django.contrib import admin
from .models import Movie, Favorite

# Register your models here.
admin.site.register(Movie)
# admin.site.register(Favorite)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie')
