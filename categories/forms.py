from builtins import super

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit, Div
from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Category Name'}))
    icon = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Icon Class'}))
    photo = forms.ImageField(label='', required=False, widget=forms.ClearableFileInput(attrs={'placeholder': 'Photo'}))
    description = forms.CharField(label='', max_length=1024,
                                  widget=forms.Textarea(attrs={'placeholder': 'Description'}))

    class Meta:
        model = Category
        fields = ('name', 'icon', 'photo', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='mt-10 form-group col-md-6 mb-0'),
                Column('icon', css_class='mt-10 form-group col-md-6 mb-0'),
                css_class='form-group'
            ),
            Div(
                Div('photo', css_class='margin-top-10 upload-header btn btn-outline-secondary',
                    style='padding: 0;'),
                # style="background: white;",
                css_class='form-group text-center'
            ),
            Div('description', css_class='form-group'),
            Submit('submit', 'Submit'),

        )
