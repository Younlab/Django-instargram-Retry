from django import forms

from posts.models import Post


class PostForm(forms.Form):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    #
    # img_field = forms.FileField(
    #     widget=forms.ImageField()
    # )

    def post_edit(self):
        contents = self.cleaned_data['content']
        imgas = self.cleaned_data['img_field']

        Post.objects.create(
            content=contents,
            photo=imgas,
        )