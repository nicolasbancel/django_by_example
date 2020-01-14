from django.contrib.sitemaps import Sitemap
from .models import Post

# frequency: change frequency of the posts
# priority: set between 0 and 1
# location is by default the url (obtained with get_absolute_url)

class PostSitemap(Sitemap):
   changefreq = 'weekly'
   priority = 0.9
   def items(self):
       return Post.published.all()
   def lastmod(self, obj):
       return obj.publish
