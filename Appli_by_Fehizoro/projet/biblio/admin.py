from django.contrib import admin
from biblio.models import Livre

# Register your models here.
#@admin.register(Livre)

class LivreAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "nbPages",
    )
    search_fields = ('titre',)

admin.site.register(Livre)