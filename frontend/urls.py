from django.urls import path
from django.conf.urls import url 
from frontend import views


app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog-page/', views.blog, name='blog'),
    path('filter-data/', views.filter_data, name='filter_data'),
    path('blogdetails-page/<int:pk>', views.blogdetails, name='blogdetails'),
    path('contact-page/', views.contact, name='contact'),
    # path('login-page/', views.login, name='login'),
]
