from django.urls import path
from .import views

app_name = 'blogapp'

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('contact/',views.contact, name='Contact'),
    path('health/',views.HealthListView.as_view(), name='Health'),
    path('sports/',views.SportsListView.as_view(), name='Sports'),
    path('food/',views.FoodListView.as_view(), name='Food'),
    path('science/',views.ScienceListView.as_view(), name='Scince'),
    path('technology/',views.TechnologyListView.as_view(), name='Technology'),
    path('banking/',views.BankingListView.as_view(), name='Banking'),
    path('environment/',views.EnvironmentListView.as_view(), name='Environment'),
    path('tourist/',views.TouristListView.as_view(), name='Tourist'),
    path('tv/',views.TVListView.as_view(), name='TV'),
    path('search/', views.search, name='Search'),
    path('signup/', views.handleSignUp, name='handleSignUp'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),
    path('postComment/', views.postComment, name='postComment'),
]
