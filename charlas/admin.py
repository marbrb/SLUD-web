from django.contrib import admin

from .models import Charla
from .models import Ponente

class PonenteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'trabajo'
    )

    search_fields = (
        'nombre',
    )


class CharlaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'descripcion',
        'fecha',
        'hora',
        'lugar',
    )

    search_fields = (
        'titulo',
        'descripcion',
    )


admin.site.register(Ponente, PonenteAdmin)
admin.site.register(Charla, CharlaAdmin)
