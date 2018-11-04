from django.core.management.base import BaseCommand
from articles.models import Article


class Command(BaseCommand):
    help = 'Populate articles fron news api top headlines.'

    def handle(self, *args, **options):
        Article.get_top_headlines()

