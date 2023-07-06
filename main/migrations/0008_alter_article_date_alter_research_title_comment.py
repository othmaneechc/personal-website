# Generated by Django 4.1.7 on 2023-02-25 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='research',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('comment', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.article')),
            ],
        ),
    ]