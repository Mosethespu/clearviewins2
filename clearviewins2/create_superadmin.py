import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clearviewins2.settings')
django.setup()
from django.contrib.auth import get_user_model

User = get_user_model()

def create_super_admin():
    username = 'superadmin'
    email = 'superadmin@clearinsure.com'
    password = 'SuperSecure!2025'
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print('Super admin created.')
    else:
        print('Super admin already exists.')

if __name__ == '__main__':
    create_super_admin()