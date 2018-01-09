from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Story, Rating
from .forms import StoryForm


def index(request):
    """
    View for render the page with five latest stories
    """

    latest_stories = Story.objects.order_by('-created_at')[:5]
    context = {"latest_stories": latest_stories}
    return render(request, 'stories/index.html', context)


def story(request, story_id):
    """
    View for render the page that display a story given its id
    """

    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'stories/story.html', {"story": story})


def add_rating(request, story_id):
    """
    View for add a rating for a given story
    """

    story = get_object_or_404(Story, pk=story_id)
    try:
        value = request.POST['rating']
    except KeyError:
        # Redisplay the story.
        return render(request, 'stories/story.html', {
            'story': story,
            'error_message': "You didn't enter a valid number(1-5).",
        })
    else:
        r = Rating(story_id=story.id, value=value)
        r.save()
        # To prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('stories:ratings',
                                            args=(story.id,)))


def ratings(request, story_id):
    """
    View to render a page with the total number of rating for a given story
    """
    story = get_object_or_404(Story, pk=story_id)
    ratings_list = Rating.objects.filter(story_id=story_id)
    values = [rating.value for rating in ratings_list]
    return render(request, 'stories/ratings.html', {"total": sum(values),
                                                    "story": story, })


def create(request):
    """
    View for create a new story
    """
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save()
            return redirect('stories:story', story_id=story.id)
    else:
        form = StoryForm()
        return render(request, 'stories/create.html', {"form": form})



