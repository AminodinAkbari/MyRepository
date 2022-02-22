from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام کاربری','class':'rtl'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور','class':'rtl'}),
    )

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام','class':'rtl','maxlength':'80'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی','class':'rtl','maxlength':'120'}),
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'تلفن','class':'rtl','maxlength':'11'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور','class':'rtl'}),
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'تکرار رمز عبور','class':'rtl'}),
    )

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if len(password)<8:
            raise forms.ValidationError('کلمه عبور باید حداقل 8 کاراکتر باشد')

        if password != re_password :
            raise forms.ValidationError('کلمه های عبور با یکدیگر مغایرت دارند')
        return password

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exist = User.objects.filter(username=phone).exists()
        if len(phone) != 11:
            raise forms.ValidationError('شماره وارد شده صحیح نیست')
        if is_exist:
            raise forms.ValidationError('شما قبلا در سایت ثبت نام کرده اید')

        return phone