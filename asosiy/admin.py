from django.contrib import admin
from .models import *

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["id","nom","davlat","prezident","murabbiy"]
    list_display_links = ["nom"]
    list_editable = ["prezident","murabbiy"]
    search_fields = ["nom"]
    search_help_text = "Club nomi bo'yicha qiring "


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id","ism","pozitsiya","club","narx","davlat","t_yil"]
    list_display_links = ["ism"]
    list_editable = ["club","narx"]
    search_fields = ["ism","davlat"]
    search_help_text = "Player ismi yoki davlati bo'yicha qidiring"


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ["id","player","eski_club","yangi_club","narx","tax_narx","mavsum"]
    list_editable = ["narx","tax_narx","mavsum"]
    autocomplete_fields = ["player","eski_club","yangi_club"]

@admin.register(Hozirgi_mavsum)
class Hozirgi_mavsumAdmin(admin.ModelAdmin):
    list_display = ["h_mavsum"]






