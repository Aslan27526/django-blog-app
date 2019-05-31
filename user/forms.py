from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(label="Istifadeci adi")
    password=forms.CharField(label="Sifre",widget=forms.PasswordInput)

    
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="İstifadəçi adı")
    password=forms.CharField(max_length=20,label="Şifrə",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Şifrəni təsdiq edin",widget=forms.PasswordInput)
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifrələr eyni deyil")
        
        values={
            "username": username,
            "password": password
        }
        return values 