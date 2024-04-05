from django import forms
from .models import Movie

# Dont put field before the input
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].required = False

