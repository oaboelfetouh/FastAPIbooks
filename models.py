from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from passlib.hash import bcrypt


class user(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)
    
    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)
    
user_pydantic = pydantic_model_creator(user, name='user')
userIn_pydantic = pydantic_model_creator(user, name='userIn', exclude_readonly=True)

class admin(user):
    pass

admin_pydantic = pydantic_model_creator(admin, name='admin')

class book(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(50, unique = True)
    Author = fields.CharField(50)
    # date_of_issue = ...

book_pydantic = pydantic_model_creator(book, name='book')
bookIn_pydantic = pydantic_model_creator(book, name='bookIn', exclude_readonly=True)
