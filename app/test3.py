# test.py


import os
import unittest

from views import app, db
from config import basedir
from models import User, Task

TEST_DB = 'test.db'


class AllTests(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            #os.path.join(basedir, TEST_DB)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/task'
        self.app = app.test_client()
        #db.create_all()

    #####################Helpers ==================
    def login(self, name, password):
        return self.app.post('/', data=dict(
            name=name, password=password), follow_redirects=True)

    def create_user(self, name, email, password):
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()


    def register(self, name, email, password, confirm):
        return self.app.post('register/', data=dict(
            name=name, email=email,
            password=password, confirm=confirm), follow_redirects=True)

    def logout(self):
        return self.app.get('logout/', follow_redirects=True)


    def create_task(self):
        return self.app.post('add/', data=dict(
            name='Go to Puerto Escondido',
            due_date='02/05/2015',
            priority='1',
            posted_date='02/04/2015',
            status='1'
        ), follow_redirects=True)








    ###################### TESTERS ################
    '''
    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please sign in to access your task list', response.data)
        '''


    '''
    def test_user_setup(self):
        new_user = User("mherman", "michael@mherman.org", "michaelherman")
        db.session.add(new_user)
        db.session.commit()
        '''
    '''
    def test_users_can_register(self):
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == "lalo"

    
    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn('Invalid username or password.', response.data)
        

    
    def test_users_can_login(self):
        self.register('manomano', 'michael@realpython.com', 'python', 'python')
        response = self.login('manomano', 'python')
        self.assertIn('You are logged in. Go Crazy.', response.data)


    def test_invalid_form_data(self):
        self.register('manomano', 'michael@realpython.com', 'python', 'python')
        response = self.login('alert("alert box!");', 'foo')
        self.assertIn('Invalid username or password.', response.data)
    '''

    def test_users_can_add_tasks(self):
        self.create_user('Danae1', 'Danae1@realpython.com', 'Danae1')
        self.login('Danae1', 'Danae1')
        self.app.get('tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn(
            'New entry was successfully posted. Thanks.', response.data
        )



if __name__ == "__main__":
    unittest.main()