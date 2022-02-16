from django import forms

class ReviewForm(forms.Form):
	comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'متن نظر'}),
    )