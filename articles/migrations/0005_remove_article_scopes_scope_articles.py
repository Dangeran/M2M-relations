# Generated by Django 4.2.1 on 2023-05-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_scope_articles_article_scopes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
        migrations.AddField(
            model_name='scope',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', to='articles.article'),
        ),
    ]
