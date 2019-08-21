from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.emmanuel= Editor(first_name = 'Emmanuel', last_name ='Muchiri', email ='emmanuel.muchiri@outlook.com')

    def test__instance(self):
        self.assertEquals(self.emmanuel.first_name,"Emmanuel")

    def test_save_method(self):
        self.emmanuel.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)
    
    # def test_delete(self):
    #     self.emmanuel.delete_editor()

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.emmanuel= Editor(first_name = 'Emmanuel', last_name ='Muchiri', email ='emmanuel.muchiri@outlook.com')
        self.emmanuel.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.emmanuel)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

        