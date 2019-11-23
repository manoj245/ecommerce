from django.db import models
class Register(models.Model):
    name= models.CharField(primary_key=True,max_length=10)
    mobno = models.IntegerField()
    email= models.EmailField()
    username= models.CharField(max_length=10)
    pwd= models.CharField(max_length=10)
    cpwd= models.CharField(max_length=10)
    def get_user1(self):
        return self.name
    def get_mobno1(self):
        return self.mobno
    def get_email1(self):
        return self.email
    def get_username1(self):
        return self.username
    def get_pwd1(self):
        return self.pwd
    def get_cpwd1(self):
        return self.cpwd
class Signin(models.Model):
    uname = models.CharField(max_length=10)
    pwd = models.CharField(max_length=10)
    def get_user(self):
        return self.uname
    def get_pwd(self):
        return self.pwd





