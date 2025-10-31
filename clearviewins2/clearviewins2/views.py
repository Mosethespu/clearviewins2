from django.core.paginator import Paginator
from django.contrib.auth.models import User
def user_management(request):
    # Show user type selection
    return render(request, 'admin/admindashboard.html', {'user_types': True})

def user_management_type(request, usertype):
    # For now, use Django's User model and filter by a dummy field or group
    # In a real app, you would have a user profile or type field
    if usertype == 'normal':
        users = User.objects.filter(is_superuser=False, is_staff=False)
        title = 'Normal Users'
    elif usertype == 'insurance':
        users = User.objects.filter(groups__name='Insurance')
        title = 'Insurance Employees'
    elif usertype == 'regulator':
        users = User.objects.filter(groups__name='Regulator')
        title = 'Regulator Users'
    else:
        users = User.objects.none()
        title = 'Unknown Type'
    paginator = Paginator(users, 10)  # 10 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin/user_management_table.html', {
        'page_obj': page_obj,
        'usertype': usertype,
        'title': title,
    })
from django.contrib.auth import logout as auth_logout
def logout(request):
    auth_logout(request)
    return redirect('/')
def admindashboard(request):
    return render(request, 'admin/admindashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def landing(request):
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def blog(request):
    return render(request, 'blog.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        # Basic validation for blank fields
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'login.html')
        # Prevent SQL injection by only allowing alphanumeric usernames (Django ORM is safe, but extra check)
        import re
        if not re.match(r'^[\w.@+-]+$', username):
            messages.error(request, 'Invalid username or email format.')
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser and user.username == 'superadmin':
                return redirect('/admindashboard/')
            # Redirect other users as needed
            return redirect('/')
        else:
            messages.error(request, 'Invalid username/email or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
