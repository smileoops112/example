from django import forms


class FeedBackForm(forms.Form):

    name = forms.CharField()
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'columns': 10}))