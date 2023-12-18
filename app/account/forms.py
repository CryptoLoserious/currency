from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSignUpForm(forms.ModelForm):

    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        cleaned_data: dict = super().clean()

        if not self.errors:
            if cleaned_data['password1'] != ['passwords2']:
                raise forms.ValidationError('Password should match!')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.save()
        return User

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )