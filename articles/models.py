import datetime

from django.db import models
from django.conf import settings
from newsapi import NewsApiClient


class Article(models.Model):
    source_id = models.SlugField(max_length=80, null=True, blank=True)
    source_name = models.CharField(max_length=100)
    author = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    url_to_image = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField()
    content = models.TextField()

    class Meta:
        ordering = ("-published_at",)

    @classmethod
    def get_top_headlines(cls):
        newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
        top_headlines = newsapi.get_top_headlines(language='en', country='us')
        articles = top_headlines.get('articles', [])
        news_headlines = []
        batch_size = top_headlines.get('totalResults', 20)

        for article in articles:
            source = article['source']
            source_id = source['id']
            source_name = source['name']
            author = article['author']
            title = article['title']
            description = article['description']
            url = article['url']
            url_to_image = article['urlToImage']
            published_at = datetime.datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            print(article)
            news_article = cls(
                source_id=source_id,
                source_name=source_name,
                author=author,
                title=title,
                description=description,
                url=url,
                url_to_image=url_to_image,
                published_at=published_at,
            )

            news_headlines.append(news_article)

        return cls.objects.bulk_create(news_headlines, batch_size)


