from markdown import markdown
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
import datetime
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()

    class Admin:
        pass

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['title']
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save()
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug


class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
    (LIVE_STATUS, 'Live'),
    (DRAFT_STATUS, 'Draft'),
    (HIDDEN_STATUS, 'Hidden'),
    )
    class Meta:
        verbose_name_plural = "Entries"
    
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,default='', on_delete=models.CASCADE)
    excerpt = models.TextField(blank=True, help_text="A short summary of the entry, Optional")
    body = models.TextField()
    #Fields to store generated html
    body_html = models.TextField(editable=False, blank=True)
    excerpt_html = models.TextField(editable=False, blank=True)
    featured = models.BooleanField(default=False)
    enable_comments = models.BooleanField(default=True)
    #pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(blank=True,)
    categories = models.ManyToManyField(Category)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html= markdown(self.excerpt)
        super(Entry, self).save()