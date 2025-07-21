from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class ExampleForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
 