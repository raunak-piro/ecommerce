from django.db import models
class Maincategory(models.Model):
	id= models.AutoField(primary_key=True)
	name = models.CharField(max_length=245)
	def __str__(self):
		return self.name
class Subcategory(models.Model):
	id= models.AutoField(primary_key=True)
	name = models.CharField(max_length=245)
	def __str__(self):
		return self.name
class Brand(models.Model):
	id= models.AutoField(primary_key=True)
	name = models.CharField(max_length=245)
	def __str__(self):
		return self.name
class Product(models.Model):
	id= models.AutoField(primary_key=True)
	name = models.CharField(max_length=245)
	maincategory = models.ForeignKey(Maincategory,on_delete = models.CASCADE)
	subcategory = models.ForeignKey(Subcategory,on_delete = models.CASCADE)
	brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
	color = models.CharField(max_length=20)
	size = models.CharField(max_length=20)
	stock = models.CharField(max_length=20,default= "In Stock" , null=True,blank=True)
	description = models.TextField()
	baseprise = models.IntegerField()
	discount = models.IntegerField(default= 0 ,null=True,blank=True)
	finalprise = models.IntegerField()
	pic1 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
	pic2 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
	pic3 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
	pic4 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
	def __str__(self):
		return self.name
class Buyer(models.Model):
	id= models.AutoField(primary_key=True)
	name = models.CharField(max_length=245)
	username = models.CharField(max_length=245)
	email = models.EmailField(max_length=245)
	phone = models.CharField(max_length=245)
	addressline1 = models.CharField(max_length=245)
	addressline2 = models.CharField(max_length=245)
	addressline3 = models.CharField(max_length=245)
	pin = models.CharField(max_length=245)
	city = models.CharField(max_length=245)
	state = models.CharField(max_length=245)
	pic4 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
	
	def __str__(self):
		return str(self.id) + "" + self.username
