from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# 博客类别
from django.utils.html import strip_tags
import markdown


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# 博客标签
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    picture = models.ImageField(verbose_name='封面')
    excerpt = models.CharField(max_length=200, blank=True, null=True, verbose_name='简介')

    # 帖子浏览数
    views = models.PositiveIntegerField(default=0)

    # 创建时间和更新时间。
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    # 定义关联关系
    category = models.ForeignKey('Category', verbose_name='类别')
    tag = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    author = models.ForeignKey(User, verbose_name='作者')

    def __str__(self):
        return self.title


    # 自动生成文章摘要,复写save方法
    def save(self, *args, **kwargs):
        # 如果没有生成文章摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 30 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.content))[:30]
            # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)



    # 自定义get_absolute_url方法，用于获取post的url
    def get_absolute_url(self):
        # /post/1/
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 帖子浏览数自加一
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        verbose_name_plural = '帖子'
        verbose_name = '帖子'
        ordering = ['-created_time']