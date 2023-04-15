from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float, ARRAY
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///mydatabase.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Create your models here.
class User(models.Model):
        username = models.CharField(max_length=50)
        password = models.CharField(max_length=128)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(null=True)
        deleted_at = models.DateTimeField(null=True)

        def __str__(self):
            return self.username


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.TextField()
    avatar = models.ImageField(upload_to='uploads/', null=True, blank=True)
    years_of_experience = models.FloatField()
    skills = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password = Column(String(128))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))
    avatar = Column(String(50), nullable=True)
    years_of_experience = Column(Float)
    skills = Column(ARRAY(String))
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)