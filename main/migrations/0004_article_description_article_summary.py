# Generated by Django 4.1.7 on 2023-02-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_research'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
