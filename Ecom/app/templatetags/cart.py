from django import template
# creating custome templete filter where filter name is function name
register = template.Library()
# it is decorator which is registering function in template
# cart have product keys in which funtion parameters product match with cart product keys or not


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    # if cart product id is equal to product id then cart mah product xa true else false
    keys = cart.keys()

    print(keys)
    for id in keys:

        if int(id) == product.id:
            return True

    return False


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:

            return cart.get(id)
    return 0
