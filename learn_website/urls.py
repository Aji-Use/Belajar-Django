
from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('library/', include('library.urls')),
    path('manager/', include('manager.urls')),
    path('blog/', include('blog.urls'))
]
