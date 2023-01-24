from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ris_list, name='ris-list'),
    path('export/excel', views.export_xls, name='ris-excel'),
    path('edit/<int:pk>', views.ris_edit, name='ris-edit'),
    path('api/smrp', views.smrp_api, name='smrp-list'),
    path('api/progress', views.progress, name='progress-list'),
]
