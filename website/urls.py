from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"), #points to contact.html, now we need a view to render our request
    path('about.html', views.about, name="about"),
    path('pricing.html',views.pricing, name="pricing"),
    path('service.html', views.service, name="service"),
    path('blog.html', views.blog, name="blog"),
    path('blog-details.html', views.blog, name="blog_details"),
    path('appointment.html', views.appointment, name="appointment"), 

]
