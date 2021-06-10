from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from frontend.models import *
from backend.forms import *

from django.contrib.auth import update_session_auth_hash

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# # from backend.forms import CommentForm
# from backend.forms import ReviewForm
from django.db.models import Count, Q


# Password Reset
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode

# Create your views here.


def register(request):
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            register.save()
            messages.success(request, 'User have been Registered')
    else:
        register = RegisterForm()
    return render(request, 'frontend/register.html', {'reg': register})


def categroy_form(request):
    if request.method == 'POST':
        cat_form = CategroyForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, 'Categroy Created.')
    else:
        cat_form = CategroyForm()
    return render(request, 'backend/add-product.html', {'cat':cat_form})






def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')


@login_required(login_url='/dashboard/')
def dashboard(request):
    return render(request, 'backend/index.html')



def add_listing(request):
    return render(request, 'backend/add_listing.html')

def bookings(request):
    return render(request, 'backend/bookings.html')

def bookmarks(request):
    return render(request, 'backend/bookmarks.html')

def charts(request):
    return render(request, 'backend/charts.html')




def reviews(request):
    return render(request, 'backend/reviews.html')

def tables(request):
    return render(request, 'backend/tables.html')

@login_required(login_url='/dashboard/')
def user_profile(request):
    
    return render(request, 'backend/user-profile.html', {'profile':request.user})
    
@login_required(login_url='/dashboard/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')

@login_required(login_url='/dashboard/')
def edit_newform(request):
    if request.method == 'POST':
        edit_form = EditUserForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'User edited successfully.')
    else:
        edit_form = EditUserForm(instance=request.user)
    return render(request, 'backend/edit-profile.html', {'edit_key':edit_form})


def reset(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/change-password.html', {'pass_key':pass_form})


def blog_form(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.user = request.user
            blog.save()
            messages.success(request, 'blog Posted')
    else:
        blog_form = BlogForm()
    return render(request, 'backend/add-blog.html', {'blog':blog_form})

login_required(login_url='/dashboard/')
def edit_blog(request, blog_id):
    single_blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        edit_form = EditBlog(request.POST, request.FILES, instance=single_blog)
        if edit_form.is_valid():
            blogf = edit_form.save(commit=False)
            blogf.user = request.user
            blogf.save()
            messages.success(request, 'Blog edited successfully.')
    else:
        edit_form = EditBlog(instance=single_blog)
    return render(request, 'backend/edit-blog.html', {'edit_key':edit_form})


def view_blog(request):
    # list_port = Portfolio.objects.order_by(-date)
    list_blog = Blog.objects.all()
    return render(request, 'backend/view-blog.html', {'list':list_blog})
    
def delete_blog(request, blog_id):
    post_record = get_object_or_404(Blog, id=blog_id)
    post_record.delete()
    return redirect('backend:view_blog')


def view_blogdetails(request, pk):
    single_post = get_object_or_404(Blog, pk=pk)
    return render(request, 'backend/view-blogdetail.html', {'sipst':single_post})

def pass_form(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/pass-form.html', {'pass_key':pass_form})

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "backend/password-reset-email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'ogunburebusayo.j@gmail.com' , [user.email])
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="backend/password-reset.html", context={"password_reset_form":password_reset_form})

def Portfolio_form(request):
    if request.method == 'POST':
        port_form = PortfolioForm(request.POST, request.FILES)
        if port_form.is_valid():
            port = port_form.save(commit=False)
            port .user = request.user
            port .save()
            messages.success(request, 'Port Posted')
    else:
        port_form = PortfolioForm()
    return render(request, 'backend/add-Portfolio.html', {'port': port_form})

login_required(login_url='/dashboard/')
def edit_portfolio(request, port_id):
    single_port  = get_object_or_404(Portfolio, id=port_id)
    if request.method == 'POST':
        edit_form = EditPort (request.POST, request.FILES, instance=single_port )
        if edit_form.is_valid():
            portf = edit_form.save(commit=False)
            portf.user = request.user
            portf.save()
            messages.success(request, 'port edited successfully.')
    else:
        edit_form = EditPortfolio (instance=single_port )
    return render(request, 'backend/edit-Portfolio.html', {'edit_key':edit_form})


def view_Portfolio(request):
    # list_port = Portfolio.objects.order_by(-date)
    list_port  = Portfolio.objects.all()
    return render(request, 'backend/view-Portfolio.html', {'list':list_port })


def delete_Portfolio(request, port_id):
    single_delete= get_object_or_404(Portfolio, pk=port_id)
    single_delete.delete()
    return redirect('backend:view_Portfolio')

def view_Portfoliodetails(request, pk):
    single_post = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'backend/view-Portfoliodetail.html', {'sipst':single_post})

def Post_form(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post Posted')
    else:
        post_form = PostForm()
    return render(request, 'backend/add-Post.html', {'post':post_form})    


login_required(login_url='/dashboard/')
def edit_Post(request, post_id):
    single_post  = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        edit_form = Editpost (request.POST, request.FILES, instance=single_post )
        if edit_form.is_valid():
            postf = edit_form.save(commit=False)
            postf.user = request.user
            postf.save()
            messages.success(request, 'post edited successfully.')
    else:
        edit_form = EditPost (instance=single_post )
    return render(request, 'backend/edit-Post.html', {'edit_key':edit_form})


def view_Post(request):
    # list_port = Portfolio.objects.order_by(-date)
    list_add  = Post.objects.all()
    return render(request, 'backend/view-Post.html', {'list':list_add })


def delete_Post(request, post_id):
    single_delete= get_object_or_404(Post, pk=post_id)
    single_delete.delete()
    return redirect('backend:view_Post')

def view_Postdetails(request, pk):
    single_post = get_object_or_404(Post, pk=pk)
    return render(request, 'backend/view-Postdetail.html', {'sipst':single_post})

def Mudia_form(request):
    if request.method == 'POST':
        mudia_form = MudiaForm(request.POST, request.FILES)
        if mudia_form.is_valid():
            mudia = mudia_form.save(commit=False)
            mudia.user = request.user
            mudia.save()
            messages.success(request, 'mudia Posted')
    else:
        mudia_form = MudiaForm()
    return render(request, 'backend/add-Mudia.html', {'mudia': mudia_form})

login_required(login_url='/dashboard/')
def edit_Mudia(request, pst_id):
    single_pst  = get_object_or_404(Mudia, id=pst_id)
    if request.method == 'POST':
        edit_form = EditMudia (request.POST, request.FILES, instance=single_pst )
        if edit_form.is_valid():
            pstf = edit_form.save(commit=False)
            pstf.user = request.user
            pstf.save()
            messages.success(request, 'mudia edited successfully.')
    else:
        edit_form = EditMudia (instance=single_pst )
    return render(request, 'backend/edit-Mudia.html', {'edit_key':edit_form})


def view_Mudia(request):
    # list_port = Portfolio.objects.order_by(-date)
    list_pst  = Mudia.objects.all()
    return render(request, 'backend/view-Mudia.html', {'list':list_pst })

def delete_Mudia(request, pst_id):
    single_delete= get_object_or_404(Mudia, pk=pst_id)
    single_delete.delete()
    return redirect('backend:view_Mudia')

def view_Mudiadetails(request, pk):
    single_post = get_object_or_404(Mudia, pk=pk)
    return render(request, 'backend/view-Mudiadetail.html', {'sipst':single_post})

def About_form(request):
    if request.method == 'POST':
        about_form = AboutForm(request.POST, request.FILES)
        if about_form.is_valid():
            about = about_form.save(commit=False)
            about.user = request.user
            about.save()
            messages.success(request, 'about Posted')
    else:
        about_form = AboutForm()
    return render(request, 'backend/add-About.html', {'about':about_form})

login_required(login_url='/dashboard/')
def edit_About(request, about_id):
    single_about = get_object_or_404(About, id=about_id)
    if request.method == 'POST':
        edit_form = EditAbout(request.POST, request.FILES, instance=single_about)
        if edit_form.is_valid():
            aboutf = edit_form.save(commit=False)
            aboutf.user = request.user
            aboutf.save()
            messages.success(request, 'about edited successfully.')
    else:
        edit_form = EditAbout(instance=single_about)
    return render(request, 'backend/edit-About.html', {'edit_key':edit_form})


def view_About(request):
    # list_port = Portfolio.objects.order_by(-date)
    list_about  = About.objects.all()
    return render(request, 'backend/view-About.html', {'list':list_about })

def delete_About(request, about_id):
    single_delete= get_object_or_404(About, pk=about_id)
    single_delete.delete()
    return redirect('backend:view_About')

def view_Aboutdetails(request, pk):
    single_post = get_object_or_404(About, pk=pk)
    return render(request, 'backend/view-Aboutdetail.html', {'sipst':single_post})

def Addpic_form(request):
    if request.method == 'POST':
        addpic_form = AddpicForm(request.POST, request.FILES)
        if addpic_form.is_valid():
            addpic =addpic_form.save(commit=False)
            addpic.user = request.user
            addpic.save()
            messages.success(request, 'addpic Posted')
    else:
        addpic_form = AddpicForm()
    return render(request, 'backend/add-Addpic.html', {'addpic': addpic_form})    


login_required(login_url='/dashboard/')
def edit_Addpic(request, pc_id):
    single_pc  = get_object_or_404(Addpic, id=pc_id)
    if request.method == 'POST':
        edit_form = EditAddpic (request.POST, request.FILES, instance=single_pc )
        if edit_form.is_valid():
            pcf = edit_form.save(commit=False)
            pcf.user = request.user
            pcf.save()
            messages.success(request, 'addpic edited successfully.')
    else:
        edit_form = EditAddpic (instance=single_pc )
    return render(request, 'backend/edit-Addpic.html', {'edit_key':edit_form})


def view_Addpic(request):
    # list_pc = Portfolio.objects.order_by(-date)
    list_pc  = Addpic.objects.all()
    return render(request, 'backend/view-Addpic.html', {'list':list_pc })


def delete_Addpic(request, pc_id):
    single_delete= get_object_or_404(Addpic, pk=pc_id)
    single_delete.delete()
    return redirect('backend:view_Addpic')

def view_Addpicdetails(request, pk):
    single_post = get_object_or_404(Addpic, pk=pk)
    return render(request, 'backend/view-Addpicdetails.html', {'sipst':single_post})