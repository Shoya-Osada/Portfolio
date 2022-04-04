from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),#トップページのURL
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),#詳細画面のURL  
    path('about/', views.AboutView.as_view(), name='about'), #プロフィール画面の URL
    path('contact/', views.ContactView.as_view(), name='contact'),#お問い合わせの URL
    path('thanks/', views.ThanksView.as_view(), name='thanks'),#お問い合わせ完了の URL
]