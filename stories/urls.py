from django.urls import path

from . import views

app_name = 'stories'
urlpatterns = [
    # url for /
    path('', views.index, name='index'),

    # url for /stories/
    path('stories/', views.index, name='index'),

    # url for /story/1
    path('story/<int:story_id>', views.story, name='story'),

    # url for /story/1/add_rating
    path('story/<int:story_id>/add_rating', views.add_rating, name='add_rating'),

    # url for /story/1/ratings
    path('story/<int:story_id>/ratings', views.ratings, name='ratings'),

    # url for /create/
    path('create/', views.create, name='create'),
]
