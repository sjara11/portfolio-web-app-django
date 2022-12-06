from django import forms
import projects

class ReviewForm(forms.Form):
    project = forms.ModelChoiceField(
        queryset=projects.models.Project.objects.all(), 
        widget=forms.Select(choices=projects.models.Project.objects.all(),
       )
    )
    title = forms.CharField(
        max_length=225,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title of your review"
        })
    )
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave your review"
        })
    )

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )