
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from asosiy.views import *
from stats.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('players20/', players20),
    path('england/', england),
    path('players/', players),
    path('clubs/', clubs),
    path('country_clubc/', country_clubc),
    path('tryouts/', tryouts),
    path('latest_transfers/', latest_transfers),
    path('stats/', stats),
    path('stats/transfer_record/', transfer_record),
    path('clublar/<str:nom>/', davlat_clublari),
    path('mavsum/<str:mavsum>/', season),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
