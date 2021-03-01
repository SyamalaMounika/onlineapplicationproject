from django import forms



class DetailsForm(forms.Form):
    name=forms.CharField()
    phono_no=forms.IntegerField()
    email_id=forms.EmailField()
    country=forms.CharField()
    address=forms.CharField(widget=forms.Textarea)