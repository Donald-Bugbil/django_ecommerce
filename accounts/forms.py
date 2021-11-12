from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Fieldset, Field, Div
from crispy_forms.bootstrap import StrictButton

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)


class CustomSigninForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields.keys():
            self.fields[fieldname].label = ""
            self.fields[fieldname].widget.attrs.update({
                'class': 'label'
            })
        self.helper =  FormHelper()
        self.helper.layout = Layout(

                Field("login", css_class="item", css_id="username", placeholder="Username"), 
                Field("password", css_class="item", css_id="password", placeholder="password"),
                StrictButton("login", css_class="w-100 create-account", type="submit")

        )

class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for fieldname in self.fields.keys():
            self.fields[fieldname].label=""
            self.fields[fieldname].widget.attrs.update({
                'class': 'label'
            })
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Field("username", css_class="item", css_id="username", placeholder="Username"),
            Field("email", css_class="item", css_id="email", placeholder="Email"),
            Field("password1", css_class="item", css_id="password1", placeholder="password"),
            Field("password2", css_class="item", css_id="password2", placeholder="password again"),
            StrictButton("Create Account", css_class="w-100 create-account", type="submit")
        )
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        return user

        
        
            

