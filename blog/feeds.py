from django .contrib.syndication.views import Feed
from .models import Post

class AllPostRssFeed(Feed):
    title = '小动博客'
    link =''
    def items(self):
        return Post.objects.all()
    def item_title(self, item):
        return '[%s]%s' %(item.category,item.title)
    def item_description(self, item):
        return item.content
