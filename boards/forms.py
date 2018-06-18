from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
     message = forms.CharField(
         widget=forms.Textarea(
            attrs={'rows':5, 'placeholder':'你惦冧 講黎聽吓'}
        ),
        max_length=4000,
        help_text="系四千個字咋! 前世"
     )

     class Meta:
        model = Topic
        fields = ['subject', 'message']
