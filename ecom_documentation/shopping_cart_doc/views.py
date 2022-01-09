


"""
This is a view shopping cart page
Functions name are product_page,latestProduct_page,toHighProduct_page

"""
def cart_page(request):
    """
    :param name:request
    :param type:URL
    :return:URL
	
    """
    return render(request,'order-shopping-cart.html')

def headShow_page(request):
    """
    :param name:request
    :param type:URL
    :return:URL,Dictionary
	
    """
    headImg = UiImageModel.objects.all()
    return render(request,"order-shopping-cart.html",{'images':headImg})