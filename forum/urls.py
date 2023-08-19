from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [    
    path('', views.home, name='home'),
    path('list/', views.post_list, name='post_list'),
    path('<slug:category_slug>/', views.post_list, name='post_list_by_category'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('post_create', views.post_create, name='post_create'),
    path('edit/<slug:slug>/', views.post_edit, name='post_edit'),
    path('delete/<slug:slug>/', views.post_delete, name='post_delete'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'), 
    path('like/', views.post_like, name='like'),
]

