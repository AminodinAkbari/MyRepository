from django import forms
from .models import Review
class ReviewForm(forms.Form):
    class Meta:
        model = Review
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'متن نظر'}),
    )