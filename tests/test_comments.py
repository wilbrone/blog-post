import unittest

from app.models import User,Pitch,Comment
from app import db


class CommentModelTest(unittest.TestCase):
    '''
    this is a test case for the class comments. for adding and saving new comments and to check if they are saved
    '''
    def setUp(self):
        self.user_Trial = User(username = 'Baron',password = 'potato', email = 'baron@gmail.com')
        self.new_blog = Blogs(id=1,title='Test_blog',blog='This is a test blog',user_id = self.user_Trial)

        self.new_comment = Comment(id=1,comment='Test comment',user_id=self.user_Trial,blog_id=self.new_blog)

    def tearDown(self):
        Blogs.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user_id,self.user_Trial)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)

    def test_get_comment(self):
        self.new_comment.save_comment()
        comment = Comments.get_comments(1)
        self.assertTrue(comment is not None)
