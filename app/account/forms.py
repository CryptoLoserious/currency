from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

User = get_user_model()


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data: dict = super().clean()

        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError('Password should match!')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)  # create object, without query to db

        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.save()  # save to db

        self._send_email()
        return User

    def _send_email(self):
        activate_path = reverse('account:activate', args=(self.instance.username, ))
        subject = 'Thanks for signing up!'
        body = f'''
        {settings.HTTP_METHOD}://{settings.DOMAIN}{activate_path}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [self.instance.username],
            fail_silently=False
        )
