# Generated by Django 4.1.7 on 2023-02-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_article_date_alter_research_title_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='article',
        ),
    ]
