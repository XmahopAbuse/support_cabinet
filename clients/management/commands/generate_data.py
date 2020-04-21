from django.core.management.base import BaseCommand, CommandError
from clients.models import NewClient
from mimesis import Person, Address



class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['count']
        for i in range(total):
           new_client =  NewClient(city=Address('ru').address(),name=Person('ru').full_name(),phone=Person('ru').telephone())
           new_client.save()
           print('client added ',new_client.name)