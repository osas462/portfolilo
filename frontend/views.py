from django.shortcuts import render
from frontend.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404

# for sending mail import
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
# Create your views here.


def index(request):
    tools = Portfolio.objects.all()
    new = Post.objects.all()[:4]
    see = Mudia.objects.all()[:4]
    lastest = About.objects.all()
    news = Addpic.objects.all()
    find = Addpost.objects.all()
    context = {
        'port':tools,
        'add':new, 
        'pst':see,
        'about':lastest,
        'pc':news, 
        'data':find
    
    }
    
    return render(request, 'frontend/index.html',context )
    
    
def blog(request):
    most_recent = Blog.objects.all()
    blog_news = Blog.objects.all()
    blog_post = Blog.objects.all()
    context = {'person_page_obj':blog_post ,'most_recent':most_recent}
    
    return render(request, 'frontend/blog.html',context)


def filter_data(request):
    if request.method == 'GET':
        query_form = FilterForm(request.GET)
        if query_form.is_valid():
            add_img = query_form.cleaned_data.get('add_img')
            add_title = query_form.cleaned_data.get('add_title')
            post = Blog.objects.all()
            query = Blog.objects.filter(listing_type=listing_type, add_title=add_title, add_img=add_img)
            return render(request, 'frontend/filter.html', {'q': query, 'qf': query_form})
        else:
            listing_type = query_form.cleaned_data.get('listing_type')
            add_img = query_form.cleaned_data.get('add_price')
            add_title = query_form.cleaned_data.get('add_title')
            post = Blog.objects.all()
            query = Blg.objects.filter(listing_type=listing_type, add_title=add_title, add_img=add_img)
            return render(request, 'frontend/filter.html', {'q': query, 'qf': query_form})
    else:
        query_form = FilterForm()
    return render(request, 'frontend/filter.html', {'qf':query_form}) 

def blogdetails(request, pk):
    single_post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')   
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'Contact Us Information'
        context = {
            'name':name,
            'email':email,
            'message':message
        }
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <ogunburebusayo.j@gmail.com>'
        send = mail.send_mail(subject, plain_message, from_email, [
                    'ogunburebusayo.j@gmail.com', email], html_message=html_message)
        if send:
            messages.success(request, 'Email sent')
        else:
            messages.error(request, 'Mail not sent')

          
    return render(request, 'frontend/blogdetails.html', {'sipst':single_post})
    
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')   
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'Contact Us Information'
        context = {
            'name':name,
            'email':email,
            'message':message
        }
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <ogunburebusayo.j@gmail.com>'
        send = mail.send_mail(subject, plain_message, from_email, [
                    'ogunburebusayo.j@gmail.com', email], html_message=html_message)
        if send:
            messages.success(request, 'Email sent')
        else:
            messages.error(request, 'Mail not sent')
    return render(request, 'frontend/contact.html')
