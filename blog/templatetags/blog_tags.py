from django import template
from django.db.models import Count

from blog.models import Post,Category,Tag

register = template.Library()


# 最新文章模板标签
@register.simple_tag
def get_recent_posts(num=3):
    return Post.objects.all().order_by('-created_time')[:num]

# 归档标签
@register.simple_tag
def archives(num=5):
    return Post.objects.all().dates('created_time','month',order='DESC')[:num]

# 分类标签
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)



# 标签云
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts = Count('post')).filter(num_posts__gt=0)
