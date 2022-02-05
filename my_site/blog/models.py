from django.db import models
from django.utils import timezone
from extentions.utils import geregori_to_jalali
from django.utils.html import format_html

# Create your models here.


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', verbose_name='سر دسته', default=None, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان دسته')
    slug = models.CharField(max_length=100, unique=True, verbose_name='آدرس دسته')
    status = models.BooleanField(default=True, verbose_name='نمایش دادن')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('p', "منتشر شده"),
        ('d', "پیش نویس"),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.CharField(max_length=100, unique=True, verbose_name='آدرس')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name="posts")
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to="images", verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return geregori_to_jalali(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_to_str(self):
        return ",".join([category.title for category in self.category_published()])
    category_to_str.short_description = 'دسته بندی'

    def category_published(self):
        return self.category.filter(status=True)

    def image_post_adminpage(self):
        return format_html("<img width=110 height=90 border-radius: 5px; src='{}'".format(self.image.url))

    def image_post(self):
        return format_html("<img width=150 height=130 border-radius: 5px; src='{}'".format(self.image.url))

    objects = ArticleManager()
