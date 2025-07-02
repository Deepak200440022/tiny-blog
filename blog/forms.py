from django import forms
from .models import Post

class PostFrom(forms.ModelForm):
    """
    Form for creating and editing Post instances.

    Uses Django's ModelForm to automatically generate form fields
    based on the Post model.

    Meta:
        model (Post): Specifies the model associated with this form.
        fields (tuple): Specifies the fields to include in the form: 'title' and 'text'.
    """

    class Meta:
        model = Post
        fields = ('title', 'text')
