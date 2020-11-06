"""URL's for the app"""
#Django
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

#Views
from api.views import create_data, row_list, data_list, all_data

urlpatterns = [
    path('api/v1', create_data, name='Upload'),
    path('api/v1/datasets', data_list.as_view(), name='load_data'),
    path('api/v1/rows', row_list.as_view(), name='load_row'),
    path('api/v1/all_data', all_data.as_view(), name='all_data')

]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)