# Generated by Django 2.1.3 on 2018-11-04 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
