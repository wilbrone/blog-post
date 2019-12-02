import unittest

from app.models import User,Blogs,Comments
from app import db

class UserModelTest(unittest.TestCase):
    '''
    this is a test case for the class comments. for adding and saving new comments and to check if they are saved
    '''
    def setUp(self):

        self.new_user = User(username = 'Baron',full_name = 'Wilbrone Okoth',email = 'baron@gmail.com',password = 'potato')
        self.user_Trial = User(username = 'Baron',pass_secure = 'potato', email = 'baron@gmail.com')



    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.user_Trial.username,'Baron')
        self.assertEquals(self.user_Trial.password,'potato')
        self.assertEquals(self.user_Trial.email,"baron@gmail.com")


    def tearDown(self):
        User.query.delete()
