from django.db import models
from django.forms import ModelForm


class Story(models.Model):
    """
    This models a Story. A story consists of a title, content/description.
    """
    title = models.CharField(max_length=125)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    """
    This models a Rating. A rating is a integer value between 1 to 5 that is
    given for a particular story
    """
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
