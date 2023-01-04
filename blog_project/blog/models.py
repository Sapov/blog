from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20, help_text='Заголовок')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=True)
    body = models.TextField()

    def __str__(self):
        return self.title
