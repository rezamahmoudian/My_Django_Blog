# Generated by Django 3.2.9 on 2022-02-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='special',
            field=models.BooleanField(default=False, verbose_name='مقاله ی ویژه'),
        ),
    ]