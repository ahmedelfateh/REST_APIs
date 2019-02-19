from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image',
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 200:
            raise forms.ValidationError('to long content')
        return content

    def clean(self, *args, **kwargs):
        content = self.cleaned_data.get('content', None)
        if content == "":
            content = None
        image = self.cleaned_data.get("image", None)
        if content is None and image is None:
            raise forms.ValidationError('Content or Image required.')
        return super().clean(*args, **kwargs)
