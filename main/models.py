from django.db import models

# Create your models here.

class Article(models.Model):
    AR_TYPE = (
        ('Article', 'Article'),
        ('Story', 'Story')
        )
    title = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=7, choices=AR_TYPE)
    date = models.DateTimeField()
    description = models.TextField(null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

    def total_comments(self):
        return self.comments.count()

class Research(models.Model):
    title = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=200)
    article = models.ForeignKey(Article, related_name="comments", null=True, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# class Users(models.Model):
#     first_name = 
#     last_name = 
#     username = 
#     password = 
