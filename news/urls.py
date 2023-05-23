from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HomePageView.as_view(), name="home"),
    path('', views.home, name="home"),
    path('news/', views.news_list, name="news_list"),
    path('blog/', views.blog, name="blog"),
    path('news/<slug:news>/', views.detail, name="detail"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('category/', views.category, name="category"),
    path('sport/', views.SportNewsView.as_view(), name="sport"),
    path('ilmiy/', views.SinceNewsView.as_view(), name="ilmiy"),
    path('madaniy/', views.CulturalNewsView.as_view(), name="madaniy"),
    path('xorij/', views.ForeignNewsView.as_view(), name="xorij"),
]