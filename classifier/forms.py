from django import forms

class ClassificationForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        label='Enter text to classify'
    )