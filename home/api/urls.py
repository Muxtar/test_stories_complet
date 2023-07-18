from django.urls import path
from home.api.views import (
                                test, 
                                category_view, 
                                category_view_id,
                                StoryView,
                                StoryViewSlug
                                )

urlpatterns = [
    # path('', test, name = 'test'),
    path('categories/', category_view, name = 'category_api'),
    path('categories/<int:id>/', category_view_id, name = 'category_api_id'),
    path('stories/', StoryView.as_view(), name = 'story_api'),
    path('stories/<slug:slug>/', StoryViewSlug.as_view(), name = 'story_api_slug'),

]