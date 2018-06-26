from django import forms
from .models import Author

import string


class AuthorForm(forms.ModelForm):
    name = forms.CharField(label='Name', required=True)

    class Meta:
        model = Author
        fields = ('name', 'tags')

    # this helps to trigger unique validation even if words in lowercase
    def clean_name(self):
        pre_name = self.cleaned_data['name']
        name = ' '.join(w.capitalize() for w in pre_name.translate(str.maketrans('', '', string.punctuation)).split())
        return name

    # FIXME No need to make handle attr setting, they are inherited from model attrs and from AuthorForm class fields
    # def __init__(self, *args, **kwargs):
    #     super(AuthorForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].required = True
