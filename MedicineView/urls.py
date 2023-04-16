"""import model"""

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static



"""import view"""


from registry.views import index


"""definition URL"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

