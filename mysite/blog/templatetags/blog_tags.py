from django import template
from django.db.models import Count
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

# could also rename the tag: @register.simple_tag(name='my_tag')
@register.simple_tag
def total_posts():
   return Post.published.count()

# Inclusion tag: can render a template with context variables returned by the tag
# Need to specify the template that will be rendered with the returned values:
# blog/post/latest_posts.html

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
   latest_posts = Post.published.order_by('-publish')[:count]
   return {'latest_posts': latest_posts}

@register.assignment_tag
def get_most_commented_posts(count=5):
   return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def mardown_format(text):
    return mark_safe(markdown.markdown(text))
