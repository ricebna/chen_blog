from django.test import TestCase

# Create your tests here.

from apps.blog.models import Article, Category, Tag
class ArticleTestCase(TestCase):
    def test_mon(self):

        months = Article.objects.datetimes('pub_time', 'month', order='DESC')
        self.assertEqual(0, months.count())