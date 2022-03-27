import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProThree.settings')

import django
django.setup()

import random
from faker import Faker
from app_three.models import User
fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        new_first_name = fake_name[0]
        new_last_name = fake_name[1]
        new_email = fakegen.email()


        user, _ = User.objects.get_or_create(first_name=new_first_name, last_name=new_last_name, email=new_email)


if __name__ == '__main__':
    print('Populating Database........Please Wait')
    populate(20)
    print('Populating Completed!')
