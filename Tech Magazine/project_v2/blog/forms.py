from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']  # فیلدهای فرم

# اصلاح نام فیلد به profile_picture
from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']  # اصلاح نام فیلد به profile_picture