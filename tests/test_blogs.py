import unittest

from app.models import User,Pitch,Comment
from app import db


class PitchModelTest(unittest.TestCase):
    '''
    this is a test case for the class comments. for adding and saving new comments and to check if they are saved
    '''
    def setUp(self):
        self.user_Trial = User(username = 'Baron',password = 'potato', email = 'baron@gmail.com')
        self.new_blog = Blogs(id=1,title='Test_blog',blog='This is a test blog',user_id = self.user_Trial)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'Test_blog')
        self.assertEquals(self.new_blog.blog,'This is a test blog')

    def test_save_blog(self):
        self.new_blog.save_blogs()
        self.assertTrue(len(Blogs.query.all())>0)

    def test_get_blogs(self):
        self.new_blog.save_blogs()
        saved_blog = Blogs.get_blogs()
        self.assertTrue(saved_blog is not None)

    def test_get_blog_by_id(self):
        self.new_blog.save_blogs()
        blog = Blogs.get_single_blog(1)
        self.assertTrue(blog is not None)

    def tearDown(self):
        Blogs.query.delete()
        User.query.delete()
