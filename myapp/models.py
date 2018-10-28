from django.db import models

class Student(models.Model):
	rollno=models.IntegerField()
	name=models.CharField(max_length=30)
	clas=models.CharField(max_length=30)
	class meta:
		db_table="Student"
# Create your models here.
