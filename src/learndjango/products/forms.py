import imp
from socket import fromshare
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField()
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                        attrs={
                            "class": "description",
                            "rows": 20
                        }
                    )
                )
    price       = forms.DecimalField(initial=69)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary'
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "Fuck" in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title

class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                        attrs={
                            "class": "description",
                            "rows": 20
                        }
                    )
                )
    price       = forms.DecimalField(initial=69)