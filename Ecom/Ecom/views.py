from atexit import register
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import Category, Product, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

# Create your views here.


def master(request):

    return render(request, 'master.html')


class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        product = Product.objects.all()
        category = Category.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.objects.filter(
                category=categoryID).order_by('-id')
        else:
            product = Product.objects.all()

        context = {
            'product': product,
            'category': category,



        }

        return render(request, 'index.html', context)

    def post(self, request):
        # return the product id where input id
        product = request.POST.get('product')
        # for decrement product in cart
        remove = request.POST.get('remove')

        # it return the cart which we added before and recent
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            print(quantity)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        return redirect('index')


# def index(request):
#     product = Product.objects.all()
#     category = Category.objects.all()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         product = Product.objects.filter(
#             category=categoryID).order_by('-id')
#     else:
#         product = Product.objects.all()

#     context = {
#         'product': product,
#         'category': category,


#     }

#     return render(request, 'index.html', context)


def Contact(request):
    return render(request, 'contact.html')

# for eassy understaning signup code lai refactor garya


# def validateCustmor(reg):
#     error_message = None
#     if not reg.username:
#         error_message = "Username Required!!"
#     elif len(reg.username) < 5:
#         error_message = "username must be 5 char long or more"
#     elif not reg.phone:
#         error_message = "Phone number is required!!"
#     elif len(reg.phone) < 10:
#         error_message = "phone number must be 10 digit or more"
#     elif not reg.password:
#         error_message = "password is required!"
#     elif len(reg.password) < 5:
#         error_message = "password must be 5 char long or more"
#     elif len(reg.email) < 5:
#         error_message = "Email must be 5 long or more"
#     elif reg.isExists():
#         error_message = "Email already Exists"

#     return error_message


# def registerCustmor(request):
#     postData = request.POST
#     username = postData.get('username')
#     email = postData.get('email')
#     phone = postData.get('phone')
#     password = postData.get('password')
#     error_message = None
#     reg = Customer(username=username, email=email,
#                    phone=phone, password=password)
#     error_message = validateCustmor(reg)
#     # saving
#     if not error_message:

#         reg.password = make_password(reg.password)

#         reg.save()
#         return redirect('index')
#     else:
#         data = {
#             'error': error_message,
#             # 'values': value,

#         }

#         return render(request, 'signup.html', data)


# def Signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerCustmor(request)
#         # postData = request.POST
    # username = postData.get('username')
    # email = postData.get('email')
    # phone = postData.get('phone')
    # password = postData.get('password')
    # validation
    # values = {
    #     'username': username,
    #     'email': email,
    #     'phone': phone,
    # }
    # error_message = None
    # reg = Customer(username=username, email=email,
    #                phone=phone, password=password)
    # if not username:
    #     error_message = "Username Required!!"
    # elif len(username) < 5:
    #     error_message = "username must be 5 char long or more"
    # elif not phone:
    #     error_message = "Phone number is required!!"
    # elif len(phone) < 10:
    #     error_message = "phone number must be 10 digit or more"
    # elif not password:
    #     error_message = "password is required!"
    # elif len(password) < 5:
    #     error_message = "password must be 5 char long or more"
    # elif len(email) < 5:
    #     error_message = "Email must be 5 long or more"
    # elif reg.isExists():
    #     error_message = "Email already Exists"

    # error_message = validateUser(reg)
    # saving
    # if not error_message:

    #     reg.password = make_password(reg.password)

    #     reg.save()
    #     return redirect('index')
    # else:
    #     data = {
    #         'error': error_message,
    #         # 'values': value,

    #     }

    #     return render(request, 'signup.html', data)


# def Login(request):
#     if request.method == "GET":

#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         print(customer)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             print(flag)
#             if flag:
#                 return redirect('index')
#             else:
#                 error_message = "Email or password invalid!!"
#         else:
#             error_message = "Email or password invalid!!"

#         return render(request, 'login.html', {'error': error_message})


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):

        postData = request.POST
        username = postData.get('username')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')
        error_message = None
        reg = Customer(username=username, email=email,
                       phone=phone, password=password)
        error_message = self.validateCustmor(reg)
    # saving
        if not error_message:

            reg.password = make_password(reg.password)

            reg.save()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                # 'values': value,

            }

            return render(request, 'signup.html', data)

    def validateCustmor(self, reg):
        error_message = None
        if not reg.username:
            error_message = "Username Required!!"
        elif len(reg.username) < 5:
            error_message = "username must be 5 char long or more"
        elif not reg.phone:
            error_message = "Phone number is required!!"
        elif len(reg.phone) < 10:
            error_message = "phone number must be 10 digit or more"
        elif not reg.password:
            error_message = "password is required!"
        elif len(reg.password) < 5:
            error_message = "password must be 5 char long or more"
        elif len(reg.email) < 5:
            error_message = "Email must be 5 long or more"
        elif reg.isExists():
            error_message = "Email already Exists"

        return error_message


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                return redirect('index')
            else:
                error_message = "Email or password invalid!!"
        else:
            error_message = "Email or password invalid!!"

        return render(request, 'login.html', {'error': error_message})


def Logout(request):
    request.session.clear()
    return redirect('login')

# cart class


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})
