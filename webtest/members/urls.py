from django.urls import path
from django.contrib import admin
from . import views

# urlpatterns = [
#     #path('', views.members, name='members')
#     path('members/', views.members, name='members')
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show),
    path('', views.write_in)
]
