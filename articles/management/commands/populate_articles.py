import time

from django.core.management.base import BaseCommand
from articles.models import Article


class Command(BaseCommand):
    help = 'Populate articles fron news api top headlines.'

    def handle(self, *args, **options):
        counter = 10

        while counter != 0:
            Article.get_top_headlines()
            time.sleep(1)
            counter -= 1
