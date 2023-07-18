from django.urls import path, include
from home.views import home, contact, about, stories, subscribe, create_story, single,Home

urlpatterns = [
    path('', home, name='index'),
    # path('', Home.as_view(), name='index'),
    path('stories/', stories, name = 'stories'),
    path('stories/<slug:slug>/', stories, name = 'stories'),

    path('create-stories/', create_story, name = 'create_story'),
    path('single/<slug:slug>/', single, name = 'single'),
    
    path('contact/', contact, name = 'contact'),
    path('about/', about, name = 'about'),
    path('recipes/', about, name = 'recipes'),   
    path('subscribe/', subscribe, name = 'subscribe'),


    path('api/', include('home.api.urls')),
]