from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    
    # path('/review', views.review ,name='review'),
    path('signup/', views.signup ,name='signup'),
    path('blog/', views.blog ,name='blog'),
    path('contacts/',views.contacts,name='contacts'),
    ]
