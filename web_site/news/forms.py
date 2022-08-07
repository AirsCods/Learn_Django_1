from django import forms
from news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'is_published',
            'photo',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            # 'is_published': forms.BooleanField(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
