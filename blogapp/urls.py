from django.urls import path
from .import views
from django.urls import reverse

app_name = 'blogapp'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('signup/', views.handleSignUp, name='handleSignUp'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('technology/',views.TechnologyListView.as_view(), name='technology'),
    path('travel/',views.TravelListView.as_view(), name='travel'),
    path('food/',views.FoodListView.as_view(), name='food'),
    path('sports/',views.SportsListView.as_view(), name='sports'),
    path('search/', views.search, name='search'),
    path('postComment/', views.postComment, name='postComment'),
    path('contact/',views.contact, name='contact'),
]
