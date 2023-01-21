from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from home.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home')
]
urlpatterns += staticfiles_urlpatterns()
