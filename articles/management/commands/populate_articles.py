from django.core.management.base import BaseCommand, CommandError
from .models import Articles


class Command(BaseCommand):
    help = 'Populate articles fron news api top headlines.'

    def handle(self, *args, **options):
        pass
