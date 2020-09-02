import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from faker import Faker

from fakedatabase.models import Person

fake = Faker()

def database(N=1000):
    for _ in range(N):
        name=fake.first_name()
        surname=fake.last_name()
        job=fake.job()
        # print(job)
        address=fake.address()
        email=fake.ascii_safe_email()
        description=fake.paragraph()
        
        person = Person.objects.get_or_create(name=name, surname=surname, job=job, address=address, email=email, description=description)
        # save.person()
        #return person

if __name__ == '__main__':
    database(1000)

#deneme
# fake = Faker()
# for _ in range(10):
#     print(fake.name())