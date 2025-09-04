from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .cart_module import Cart
from products.models import Product
from .models import Order, OrderItem, DiscountCode


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        color = request.POST.get('color', 'empty')
        size = request.POST.get('size', 'empty')
        quantity = request.POST.get('quantity', 1)

        cart = Cart(request)
        cart.add(quantity, color, size, product)

        return redirect('cart:cart_detail')


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, "cart/order_detail.html", {'order': order})


class OrderCreateView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item["product"],
                                     quantity=item['quantity'], color=item["color"],
                                     size=item["size"], price=item['price'])

        cart.remove_cart()
        return redirect('cart:order_detail', order.id)


class ApplyDiscountView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        code = request.POST.get('discount_code')
        # discount_code = get_object_or_404(DiscountCode, name=code)

        discount_code = DiscountCode.objects.filter(name=code).first()

        if not discount_code:
            messages.error(request, "کد تخفیف وارد شده معتبر نیست.")
            return redirect('cart:order_detail', order.id)

        if discount_code.quantity == 0:
            messages.warning(request, "این کد تخفیف دیگر قابل استفاده نیست.")
            return redirect('cart:order_detail', order.id)

        order.total_price -= order.total_price * discount_code.discount / 100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('cart:order_detail', order.id)
