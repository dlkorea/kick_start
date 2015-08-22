from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendar/', include('culture_cal.urls', namespace='calendar')),
    url(r'^langx/', include('langx.urls', namespace='langx')),
    url(r'^accounts/', include('allauth.urls')),



    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
