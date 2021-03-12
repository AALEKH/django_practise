from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique_for_date = 'publish') # Can't have two similar entry for same publish date
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('app1:post_detail', args = [self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:                  # Gives Meta Information about a class; here: django model class
        ordering = ('-publish',) # Order in descending publish date
    def __str__(self):
        return self.title

