from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site

class PostSitemap(Sitemap):
    def items(self):
        # Return a list of URLs you want to include in the sitemap
        return [
            {'url': '/', 'changefreq': 'monthly', 'priority': 1.0},  # Root URL
            {'url': '/option-strategy-builder', 'changefreq': 'monthly', 'priority': 1.0}  # /option-strategy-builder URL
        ]

    def location(self, item):
        # Return the location for each item
        return item['url']

    def changefreq(self, item):
        # Return the changefreq for each item (optional)
        return item.get('changefreq', 'monthly')

    def priority(self, item):
        # Return the priority for each item (optional)
        return item.get('priority', 1.0)
