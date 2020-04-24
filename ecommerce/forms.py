from django import forms
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
import re

User = get_user_model()


class ContactForm(forms.Form):

	name     = forms.CharField(label='Your name', max_length=100,
		       widget = forms.TextInput(
		       	        attrs = {
                             "class":"form-control input-lg" ,
                             "id":"name", "placeholder":"Your Name"
                            }
                        )
                    )
	# Default required=True
	email    = forms.EmailField(label='Your Email', max_length=100,
		       widget = forms.TextInput(
		       	        attrs = {
                             "class":"form-control input-lg" ,
                             "id":"email", "placeholder":"Your Email"
                            }
                        )
                    )
	message  = forms.CharField(label='Your Message', max_length=500,
		       widget = forms.Textarea(
		       	        attrs = {
                             "class":"form-control input-lg" ,
                             "id":"message", "placeholder":"Your Message"
                            }
                        )
                    )

	def cleaned_email(self):
		email = self.cleaned_data.get("email")
		if not 'gmail.com' in email:
			raise forms.ValidationError("Email has to be gmail.com")
		return email


class LoginForm(forms.Form):
    username = forms.CharField(label = "Username",
      	    widget = forms.TextInput(
      		    attrs = {
      		      "class"       : "form-control input-lg",
      		       "id"          : "username",
      		       "placeholder" : "username"
      		    }
      	    )
        )

    password = forms.CharField(label = "Password",
      	    widget = forms.PasswordInput(
      		    attrs = {
      		      "class"       : "form-control input-lg",
      		       "id"          : "password",
      		       "placeholder" : "password"
      		    }
      	    )
        )


class RegisterForm(forms.Form):
    username     = forms.CharField(label = "Username", max_length=100, 
                   widget = forms.TextInput(attrs = {
                    "class"       : "form-control input-lg",
                    "placeholder" : "Username"
                    })   
            )

    email     = forms.CharField(label = "Email", max_length=100, 
                   widget = forms.TextInput(attrs = {
                    "class"       : "form-control input-lg",
                    "placeholder" : "Email"
                    })   
            )

    password  = forms.CharField(label = "Password", max_length=100, 
                   widget = forms.PasswordInput(attrs = {
                    "class"       : "form-control input-lg",
                    "placeholder" : "Password"
                    })   
            )

    password2  = forms.CharField(label = "Confirm Password", max_length=100, 
                   widget = forms.PasswordInput(attrs = {
                    "class"       : "form-control input-lg",
                    "placeholder" : "Password"
                    })   
            )

    def clean_email(self):
        data      = self.cleaned_data
        email     = data.get('email')
        qs        = User.objects.filter(email=email)
        if not 'gmail.com' in email:
            raise forms.ValidationError("Email should be gmail.com")
        if qs.exists():
            msg = """This Email is registered, would you like to <a href="{link}">login</a>?
            """.format(link='/login')
            raise forms.ValidationError(mark_safe(msg))    
        return email

    def clean(self):
        data      = self.cleaned_data
        password  = data.get('password')
        password2 = data.get('password2')
        if len(password)<6:
            raise forms.ValidationError("Password length shoulde be minimum of 6 Char")
        if password != password2:
              raise forms.ValidationError("Password Mismatch")
        return data

    def clean_username(self):
        data      = self.cleaned_data
        username     = data.get('username')
        qs        = User.objects.filter(username=username)
        if qs.exists():
            msg = """This username is registered, would you like to <a href="{link}">login</a>?
            """.format(link='/singup_crud/login/')
            raise forms.ValidationError(mark_safe(msg))
        return username





