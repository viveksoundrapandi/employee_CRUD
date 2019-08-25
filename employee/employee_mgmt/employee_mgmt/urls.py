from django.conf.urls import *
from django.contrib import admin
# from django.urls import path  
from empapp import views  


urlpatterns = [
    # Examples:
    # url(r'^$', 'employee_mgmt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('emp', views.emp),  
    url('show',views.show),  
    url(r'^edit/(?P<id>\d+)/?$', views.edit),  
    url(r'^update/(?P<id>\d+)/?$', views.update),  
    url(r'^delete/(?P<id>\d+)/?$', views.destroy),  
]
