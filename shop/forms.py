from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ReviewForm(forms.Form):
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ]
    name = forms.CharField(label='Имя', required=True,
                           max_length=150,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите имя',
                                                         'class': 'form-control'
                                                         })
                           )
    text = forms.CharField(label='Текст',
                           required=False,
                           widget=forms.Textarea({'placeholder': 'Текст отзыва',
                                                  'class': 'form-control'
                                                  })
                           )
    stars = forms.ChoiceField(label='Оценка',
                              required=True,
                              widget=forms.RadioSelect(choices=CHOICES, ),
                              choices=CHOICES, )


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,
                               max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Логин',
                                                             'class': 'form-control'
                                                             }))
    email = forms.CharField(required=True,
                            max_length=150,
                            widget=forms.TextInput(attrs={'placeholder': 'E-mail',
                                                          'class': 'form-control'
                                                          }))

    password1 = forms.CharField(min_length=8, max_length=30,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Пароль',
                                           'class': 'form-control'
                                           }),
                                required=True)
    password2 = forms.CharField(min_length=8, max_length=30,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Повторите пароль',
                                           'class': 'form-control'
                                           }))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(message="Пароли не совпадают!")
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин',
                               max_length=50,
                               widget=forms.TextInput
                               )
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)


class CartAddForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

# class CartRemoveForm(forms.Form):
#
