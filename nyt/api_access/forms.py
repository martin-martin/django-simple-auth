from django import forms


class ApiCallForm(forms.Form):
    key = forms.CharField(widget=forms.widgets.TextInput(
        attrs={'placeholder': 'NYT API key'}))
