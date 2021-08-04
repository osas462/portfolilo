from django import forms
from frontend.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import FieldError


class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name*",
               widget=forms.TextInput(
               attrs={'class': 'form-control', 'placeholder': 'Enter Category'}))
    cat_desc = forms.CharField(label='Description', required=False,
               widget=forms.Textarea(
               attrs={'class': 'form-control'}
             ))
    catch_bot = forms.CharField(required=False,
                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field

    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name')
        if Category.objects.filter(cat_name=cat).exists().lower():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    # class Meta():
    #     fields = '__all__'
    #     model = 'Category'



class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'input--style-4', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput(
        attrs={'class': 'input--style-4', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'input--style-4', 'placeholder': 'Enter Password'}))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user
            

class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(label="Category Name*",
               widget=forms.TextInput(
               attrs={'class': 'form-control', 'placeholder': 'Enter Category'}))
    cat_desc = forms.CharField(label='Description', required=False,
               widget=forms.Textarea(
               attrs={'class': 'form-control'}
             ))
    catch_bot = forms.CharField(required=False,
                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # clean_<fieldname> is use to validate for just one field

    def clean_cat_name(self):
        cat = self.cleaned_data.get('cat_name')
        if Category.objects.filter(cat_name=cat).exists().lower():
            raise forms.ValidationError(f'{cat} already exist')
        return cat

    # class Meta():
    #     fields = '__all__'
    #     model = Category

class EditUserForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Username' }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
   

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['username',  'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        
        if commit:
            user.save()
            return user

class BlogForm(forms.ModelForm):


    class Meta():
        exclude = ['date', 'user']
        model = Blog

        widgets={
            'blog_title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_img': forms.FileInput(attrs={'class': 'form-control'}),
            'blog_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
           

        }



class EditBlog(forms.ModelForm):
    
    class Meta():
        model = Blog
        fields = ['blog_title', 'blog_img', 'blog_desription']

        widgets={
            'blog_title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_img': forms.FileInput(attrs={'class': 'form-control'}),
            'blog_desription': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    new_password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['new_password1', 'new_password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['new_password1']
        user.password2 = self.cleaned_data['new_password2']
        
        if commit:
            user.save()
            return user

class PortfolioForm(forms.ModelForm):


    class Meta():
        exclude = ['date', 'user']
        model = Portfolio

        widgets={
            'port_title': forms.TextInput(attrs={'class': 'form-control'}),
            'port_img': forms.FileInput(attrs={'class': 'form-control'}),
            'port_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
           

        }



class EditPortfolio(forms.ModelForm):
    
    class Meta():
        model = Portfolio
        fields = ['port_title', 'port_img', 'port_desription']

        widgets={
            'port_title': forms.TextInput(attrs={'class': 'form-control'}),
            'port_img': forms.FileInput(attrs={'class': 'form-control'}),
            'port_desription': forms.Textarea(attrs={'class': 'form-control'}),
        }



class PostForm(forms.ModelForm):


    class Meta():
        exclude = ['date', 'user']
        model = Post

        widgets={
            'add_title': forms.TextInput(attrs={'class': 'form-control'}),
            'add_img': forms.FileInput(attrs={'class': 'form-control'}),
            'add_desription': forms.Textarea(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
           

        }


class EditPost(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ['add_title', 'add_img', 'add_desription']

        widgets={
            'add_title': forms.TextInput(attrs={'class': 'form-control'}),
            'add_img': forms.FileInput(attrs={'class': 'form-control'}),
            'add_desription': forms.Textarea(attrs={'class': 'form-control'}),
        }


class MudiaForm(forms.ModelForm):


    class Meta():
        exclude = ['date', 'user']
        model = Mudia

        widgets={
            'pst_title': forms.TextInput(attrs={'class': 'form-control'}),
            'pst_img': forms.FileInput(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
           

        }


class EditMudia(forms.ModelForm):
    
    class Meta():
        model = Mudia
        fields = ['pst_title', 'pst_img']

        widgets={
            'pst_title': forms.TextInput(attrs={'class': 'form-control'}),
            'pst_img': forms.FileInput(attrs={'class': 'form-control'}),
            
        }

class AboutForm(forms.ModelForm):


    class Meta():
        exclude = ['date', 'user']
        model = About

        widgets={
            'about_title': forms.TextInput(attrs={'class': 'form-control'}),
            'about_img': forms.FileInput(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
           

        }


class EditAbout(forms.ModelForm):
    
    class Meta():
        model = About
        fields = ['about_title', 'about_img']

        widgets={
            'about_title': forms.TextInput(attrs={'class': 'form-control'}),
            'about_img': forms.FileInput(attrs={'class': 'form-control'}),
            
        }


class AddpicForm(forms.ModelForm):


    class Meta():
        exclude = ['date', 'user']
        model = Addpic

        widgets={
            'pc_title': forms.TextInput(attrs={'class': 'form-control'}),
            'pc_img': forms.FileInput(attrs={'class': 'form-control'}),
            'appear_home' : forms.Select(attrs={'class': 'form-control'}),
           

        }


class EditAddpic(forms.ModelForm):
    
    class Meta():
        model = Addpic
        fields = ['pc_title', 'pc_img']

        widgets={
            'pc_title': forms.TextInput(attrs={'class': 'form-control'}),
            'pc_img': forms.FileInput(attrs={'class': 'form-control'}),
            
        }


# class FilterForm(forms.ModelForm):
#     add_title = forms.CharField(required=False, label='Location*', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Location'}))

#     add_img = forms.CharField(required=False, label='Price*', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Price'}))

#     listing_type = forms.CharField(required=False, label='Listing Type*', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Listing Type'}))


#     class Meta():
#         exclude = ['add_desription','add_img','add_title']
#         model = Blog
