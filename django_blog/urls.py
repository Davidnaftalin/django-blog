from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^django_blog/', include('django_blog.foo.urls')),

)
