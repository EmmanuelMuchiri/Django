from django.test import TestCase
from .models import Editor,Article,tags
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
    
    def test_delete(self):
        self.emmanuel.delete_editor()
        
        