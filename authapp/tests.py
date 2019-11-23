from django.test import TestCase
from authapp.models import Signin,Register
class logintestcase(TestCase):
    def setUp(self):
        Signin.objects.create(uname="hi",pwd="hello")
    def test_Signin_info(self):
        s1=Signin.objects.get(uname="hi",pwd="hello")
        self.assertEqual(s1.get_user(),"hi")
        self.assertEqual(s1.get_pwd(),"hello")
class registertestcase(TestCase):
    def setUp(self):
        Register.objects.create(name="hi",mobno="8341130159",email="manoj@gmail.com",username="manoj",pwd="hello",cpwd="hello")
    def test_register_info(self):
        s2=Register.objects.get(name="hi",mobno="8341130159",email="manoj@gmail.com",username="manoj",pwd="hello",cpwd="hello")
        self.assertEqual(s2.get_user1(),"hi")
        self.assertEqual(s2.get_mobno1(),8341130159)
        self.assertEqual(s2.get_email1(), "manoj@gmail.com")
        self.assertEqual(s2.get_username1(), "manoj")
        self.assertEqual(s2.get_pwd1(), "hello")
        self.assertEqual(s2.get_cpwd1(), "hello")
print("success")


