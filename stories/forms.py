from django import forms

from .models import Story


class StoryForm(forms.ModelForm):
    """
    This form is for adding a new story
    """

    class Meta:
        model = Story
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '15'}),
        }
