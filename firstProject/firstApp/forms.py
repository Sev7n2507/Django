from django import forms
from .models import Question


# creating a form
class QuestionForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Question

        # specify fields to be used
        fields = [
            "text",
        ]
