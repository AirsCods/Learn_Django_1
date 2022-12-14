"""web_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from  django.views.decorators.cache import cache_page
from .views import *


urlpatterns = [
    path('test/', send_user_mail, name='test'),
    path('contacts/', send_user_mail, name='contacts'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomeNews.as_view(), name='home'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),
    # path('cat/<int:category_id>', get_category, name='category'),
    path('cat/<int:category_id>', NewsByCategory.as_view(), name='category'),
    # path('<int:news_id>/', view_news, name='view_news'),
    path('<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('add-news/', add_news, name='add_news'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
]
