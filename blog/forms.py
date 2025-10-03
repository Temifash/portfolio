from django import forms
from . import models

class CreatePost(forms.ModelForm):
  class Meta:
    model = models.NewBlog
    fields = ["title", "description", "content", "author", "image"]