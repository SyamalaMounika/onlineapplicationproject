from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Product
from testapp.forms import DetailsForm

# Create your views here.

def get_product_data(request):
    product_list=Product.objects.all()
    
    item_name=request.GET.get('item_name')#adidas
    if item_name!='' and item_name!=None:
        product_list=product_list.filter(name__contains=item_name)
   
                                        
                                        
    my_dict={'product_list':product_list}
    return render(request,"welcome.html",my_dict)


def details(request):
    form=DetailsForm()
    my_dict={'form':form}
    return render(request,"details.html",my_dict)




def payment(request):
    order_amount = 500
    order_currency = 'INR'
    client=razorpay.Client(auth=('rzp_test_iChwI2byC1ea4b','9VCVszgYNeRErWoGqDkXLm7N'))
    client.order.create(amount=order_amount, currency=order_currency)



def success(request):
    return render(request,"success.html")





