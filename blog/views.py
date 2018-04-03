from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import markdown
# Create your views here.
from django.views.generic import ListView

import mypage
from blog.models import Post, Category ,Tag
from  django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from comments.forms import CommentForm


# # 博客首页
# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request,'blog/index.html',locals())
#
# # 文章归档
# def archives(request, year, month):
#
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month,
#                                     ).order_by('-created_time')
#
#     return render(request, 'blog/index.html', locals())
# # 文章分类
# def category(request,pk):
#     cate = get_object_or_404(Category,pk=pk)
#     post_list = cate.post_set.all()
#     return render(request,'blog/index.html',locals())


# 利用通用视图类重写博客首页,归档,分类,和标签云

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 3

    # 重写get_context_data,一遍放入我们的分页的起始页面和结束页码
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 获取分页相关的变量
        page = context.get('page_obj')
        paginator = context.get('paginator')
        start , end = mypage.custompaginater(paginator.num_pages, page.number, 3)
        context.update({
            'page_range':range(start,end+1)
        })
        return context

class ArchivesView(IndexView):
    def get_queryset(self):
        return super().get_queryset().filter(created_time__year=self.kwargs.get('year'),
                                             created_time__month=self.kwargs.get('month'))

class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)

class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag,pk = self.kwargs.get('pk'))
        return super().get_queryset().filter(tag =tag)


# 博客详情
def detail(request,pk):
    post = Post.objects.get(pk = pk)
    post.increase_views()
    form = CommentForm()
    comment_list = post.comment_set.all()

    # 将 Markdown 格式的文本渲染成 HTML
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    return  render(request,'blog/detail.html',locals())


