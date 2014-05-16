from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from blog.views import HomeView, PermaView, SignUpFormView, SubmitFormView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^(?P<pk>\d+)$', PermaView.as_view(), name='detail'),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'},  name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'home'}, name='logout'),

    url(r'^register$', SignUpFormView.as_view(), name='register'),

    url(r'^submit$', login_required(SubmitFormView.as_view()), name='submit'),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^django_blog/', include('django_blog.foo.urls')),
)
