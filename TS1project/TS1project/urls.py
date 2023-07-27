from django.contrib import admin
from django.urls import path
from TS1app.views import learn_django, about, show, inputdata
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/<int:id>/', learn_django, name='django'),
    path('about/', about, name='about'),
    path('show/', show, name='show'),
    path('input/', inputdata, name='input')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)