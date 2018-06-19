from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from boards import views

urlpatterns = [
    path('',views.home, name='home'),
   # path('home/',views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('boards/<int:pk>', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
]
