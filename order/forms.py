from django import forms
from order.models import Order


class OrderCreateForm(forms.ModelForm):

    first_name = forms.CharField(label='', required=True, error_messages={'required': ''},
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя',
                                                               'class': 'form-control'
                                                               }))
    last_name = forms.CharField(label='',required=True, error_messages={'required': ''},
                                widget=forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                              'class': 'form-control'
                                                              }))
    email = forms.CharField(required=True, error_messages={'required': ''},
                            widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control'
                                                           }))
    address = forms.CharField(required=True, error_messages={'required': ''},
                              widget=forms.TextInput(attrs={'placeholder': 'Адрес',
                                                            'class': 'form-control'
                                                            }))
    postal_code = forms.CharField(required=True, error_messages={'required': ''},
                                  widget=forms.TextInput(attrs={'placeholder': 'Почтовый индекс',
                                                                'class': 'form-control'
                                                                }))
    city = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Город',
                                                         'class': 'form-control'
                                                         }))
    class Meta:
        model = Order
        fields =['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

