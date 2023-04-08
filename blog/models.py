from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
    blog_name = models.CharField(max_length=60)
    blog_description = models.CharField(max_length=160)

    def __str__(self):
        return self.blog_name


class Post(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = RichTextUploadingField()
    featured_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    featured_alt = models.CharField(max_length=100, blank=True, null=True)
    tags = TaggableManager(blank=True,)
    featured = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)
    mod_date = models.DateTimeField(auto_now_add=True)

    meta_title = models.CharField(max_length=160, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    def __str__(self):
        return self.title