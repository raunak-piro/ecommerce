from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponse
def home(request):
	data = Product.objects.all().order_by('id').reverse()[:8]
	return render(request,'index.html',{'data':data})
def shop(request,mc,sc,br):
	if (mc=='All' and sc == 'All' and br == 'All'):
		data = Product.objects.all().order_by('id').reverse()
	elif (mc!='All' and sc == 'All' and br == 'All'):
		data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by('id').reverse()
	elif (mc=='All' and sc != 'All' and br == 'All'):
		data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
	elif (mc=='All' and sc == 'All' and br != 'All'):
		data = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by('id').reverse()
	elif (mc!='All' and sc != 'All' and br == 'All'):
		data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
	elif (mc=='All' and sc != 'All' and br != 'All'):
		data = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
	elif (mc!='All' and sc == 'All' and br != 'All'):
		data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
	else:
		data = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
		
	maincategory = Maincategory.objects.all()
	subcategory = Subcategory.objects.all()
	brand = Brand.objects.all()
	return render(request,"shop.html",{'data':data,'maincategory':maincategory,	'subcategory':subcategory,'brand':brand,'mc':mc,'sc':sc,'br':br})
# Create your views here.
def singleproduct(request,id):
	data = Product.objects.get(id=id)
	return render(request,"single-product.html",{'data':data})

def loginpage(request):
	return render(request,'login.html')
def signupPage(request):
	if (request.method == "post"):
		p = request.POST.get("password")
		cp = request.POST.get("cpassword")
		if (p == cp):
			b = Buyer()
		else:
			return HttpResponse("Error")

	return render(request,'signup.html')