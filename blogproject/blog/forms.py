from django import forms
from blog.models import Comment
class EmailSendFrom(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control m-1','placeholder':'NAME'}))
    email =forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control m-1','placeholder':'Email(From)'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control m-1','placeholder':'Email(To)'}))
    comment= forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form_control m-1','placeholder':'Comment'}))

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control m-1', 'placeholder': 'NAME'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control m-1', 'placeholder': 'Email'}))
    body = forms.CharField(required=False ,widget=forms.Textarea(attrs={'class': 'form_control m-1', 'placeholder': 'Comment'}))

    class Meta:
        model=Comment
        fields=['name','email','body']
