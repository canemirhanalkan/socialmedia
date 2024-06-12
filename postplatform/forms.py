from django import forms
from django.forms import TextInput, Textarea

from postplatform.models import Posts, Comment

# class PostCreateForm(forms.Form):

#     imageUrl = forms.CharField(
#         label = "Fotoğraf", 
#         error_messages={"required":"Fotoğraf alanı zorunludur."}, 
#         widget=forms.TextInput(attrs={"class":"form-control"})
#     )


#     description = forms.CharField(
#         label="Açıklama",
#         error_messages={"required":"Açıklama alanı zorunludur."},
#         widget=forms.Textarea(attrs={"class":"form-control"})

#     )


#--- post models form ---#

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("image","description")
        labels = {
            "description":"Açıklama",
            "image":""
        }
        widgets = {
            "description": Textarea(attrs={"class":"form-control"})
        }



class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "content": ""
        }
        widgets = {
            "content": Textarea(attrs={"class":"form-control"})
        }




