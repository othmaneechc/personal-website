# Generated by Django 4.1.7 on 2023-02-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(null=True),
        ),
    ]