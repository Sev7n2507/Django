from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# creating a form
class ProductForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Product

        # specify fields to be used
        fields = [
            "name",
            "description",
            "price",
            "photo",
            "quantity",
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
