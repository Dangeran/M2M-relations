# Generated by Django 4.2.1 on 2023-05-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.AddField(
            model_name='scope',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Тег'),
        ),
    ]
