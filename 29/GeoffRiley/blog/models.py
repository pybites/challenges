from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    class Meta:
        ordering = ['-created_on']
        indexes = [
            models.Index(fields=['created_on']),
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['post', '-created_on']
        indexes = [
            models.Index(fields=['created_on']),
            models.Index(fields=['author']),
        ]

    def __str__(self):
        return f'{self.author}: {self.body[:20]}'
