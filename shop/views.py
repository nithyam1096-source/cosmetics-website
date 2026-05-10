from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Category, Product, Banner, Offer, AboutSection, Ingredient, WhyGlowifySection, WhyGlowifyFeature, Testimonial, FlashSaleBanner, NewsletterSubscription, EyeMakeupProduct, FragranceProduct, HairCareProduct, LipstickProduct, NailProduct, OfferBanner, OfferProduct, MidnightSet, AboutRightImage, AboutHeroBanner, FounderSection, ContactBanner, LoginIllustration


CART_MODELS = {
    'product': Product,
    'eye': EyeMakeupProduct,
    'fragrance': FragranceProduct,
    'hair': HairCareProduct,
    'lipstick': LipstickProduct,
    'nail': NailProduct,
}


def get_cart_product(cart_key):
    parts = cart_key.rsplit('_', 1)
    model_name = parts[0]
    product_id = int(parts[1])
    return CART_MODELS[model_name].objects.get(id=product_id, is_active=True)


def get_product_price(product):
    return float(product.discount_price) if hasattr(product, 'discount_price') and product.discount_price else float(product.price)


def get_product_image(product):
    return product.image.url if hasattr(product, 'image') and product.image else ''


def get_product_name(product):
    if hasattr(product, 'name') and product.name:
        return product.name
    if hasattr(product, 'title') and product.title:
        return product.title
    return 'Product'


def get_product_slug(product):
    return product.slug if hasattr(product, 'slug') else ''


def home(request):
    banners = Banner.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    latest_products = Product.objects.filter(is_active=True)[:8]
    active_offers = Offer.objects.filter(is_active=True)
    about_section = AboutSection.objects.filter(is_active=True).first()
    ingredients = Ingredient.objects.all()
    why_glowify = WhyGlowifySection.objects.filter(is_active=True).first()
    why_features = WhyGlowifyFeature.objects.filter(is_active=True, section=why_glowify).order_by('order') if why_glowify else []
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order')
    flash_sale = FlashSaleBanner.objects.filter(is_active=True).first()

    context = {
        'banners': banners,
        'categories': categories,
        'featured_products': featured_products,
        'latest_products': latest_products,
        'active_offers': active_offers,
        'about_section': about_section,
        'ingredients': ingredients,
        'why_glowify': why_glowify,
        'why_features': why_features,
        'testimonials': testimonials,
        'flash_sale': flash_sale,
    }
    return render(request, 'shop/home.html', context)


def shop(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)

    category_slug = request.GET.get('category')
    current_category_name = None
    if category_slug:
        products = products.filter(category__slug=category_slug)
        try:
            current_category_name = Category.objects.get(slug=category_slug).category_name
        except Category.DoesNotExist:
            pass

    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')

    context = {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
        'current_category_name': current_category_name,
        'search_query': search_query,
    }
    return render(request, 'shop/shop.html', context)


def eye_makeup(request):
    products = EyeMakeupProduct.objects.filter(is_active=True)
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    context = {
        'products': products,
        'current_category_name': 'Eye Makeup',
        'is_eye_makeup': True,
    }
    return render(request, 'shop/shop.html', context)


def eye_makeup_detail(request, slug):
    product = get_object_or_404(EyeMakeupProduct, slug=slug, is_active=True)
    related_products = EyeMakeupProduct.objects.filter(is_active=True).exclude(slug=slug)[:4]
    context = {
        'product': product,
        'related_products': related_products,
        'is_eye_makeup': True,
    }
    return render(request, 'shop/product_detail.html', context)


def fragrance(request):
    products = FragranceProduct.objects.filter(is_active=True)
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    context = {
        'products': products,
        'current_category_name': 'Fragrance',
        'is_fragrance': True,
    }
    return render(request, 'shop/shop.html', context)


def fragrance_detail(request, slug):
    product = get_object_or_404(FragranceProduct, slug=slug, is_active=True)
    related_products = FragranceProduct.objects.filter(is_active=True).exclude(slug=slug)[:4]
    context = {
        'product': product,
        'related_products': related_products,
        'is_fragrance': True,
    }
    return render(request, 'shop/product_detail.html', context)


def hair_care(request):
    products = HairCareProduct.objects.filter(is_active=True)
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    context = {
        'products': products,
        'current_category_name': 'Hair Care',
        'is_hair_care': True,
    }
    return render(request, 'shop/shop.html', context)


def hair_care_detail(request, slug):
    product = get_object_or_404(HairCareProduct, slug=slug, is_active=True)
    related_products = HairCareProduct.objects.filter(is_active=True).exclude(slug=slug)[:4]
    context = {
        'product': product,
        'related_products': related_products,
        'is_hair_care': True,
    }
    return render(request, 'shop/product_detail.html', context)


def lipstick(request):
    products = LipstickProduct.objects.filter(is_active=True)
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    context = {
        'products': products,
        'current_category_name': 'Lipsticks',
        'is_lipstick': True,
    }
    return render(request, 'shop/shop.html', context)


def lipstick_detail(request, slug):
    product = get_object_or_404(LipstickProduct, slug=slug, is_active=True)
    related_products = LipstickProduct.objects.filter(is_active=True).exclude(slug=slug)[:4]
    context = {
        'product': product,
        'related_products': related_products,
        'is_lipstick': True,
    }
    return render(request, 'shop/product_detail.html', context)


def nail(request):
    products = NailProduct.objects.filter(is_active=True)
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    context = {
        'products': products,
        'current_category_name': 'Nails',
        'is_nail': True,
    }
    return render(request, 'shop/shop.html', context)


def nail_detail(request, slug):
    product = get_object_or_404(NailProduct, slug=slug, is_active=True)
    related_products = NailProduct.objects.filter(is_active=True).exclude(slug=slug)[:4]
    context = {
        'product': product,
        'related_products': related_products,
        'is_nail': True,
    }
    return render(request, 'shop/product_detail.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(category=product.category, is_active=True).exclude(slug=slug)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/product_detail.html', context)


def offers(request):
    active_offers = Offer.objects.filter(is_active=True)
    expired_offers = Offer.objects.filter(is_active=False)
    offer_banners = OfferBanner.objects.filter(is_active=True).order_by('order')
    offer_products = OfferProduct.objects.filter(is_active=True).order_by('order')
    midnight_set = MidnightSet.objects.filter(is_active=True).first()

    context = {
        'active_offers': active_offers,
        'expired_offers': expired_offers,
        'offer_banners': offer_banners,
        'offer_products': offer_products,
        'midnight_set': midnight_set,
    }
    return render(request, 'shop/offers.html', context)


def about(request):
    hero = AboutHeroBanner.objects.filter(is_active=True).first()
    about_images = AboutRightImage.objects.filter(is_active=True)
    founder = FounderSection.objects.filter(is_active=True).first()
    return render(request, 'shop/about.html', {'hero': hero, 'about_images': about_images, 'founder': founder})


def contact(request):
    contact_banner = ContactBanner.objects.filter(is_active=True).first()
    return render(request, 'shop/contact.html', {'contact_banner': contact_banner})


def cart(request):
    cart_data = request.session.get('cart', {})
    cart_items = []
    subtotal = 0.0
    invalid_keys = []

    for key, item_data in cart_data.items():
        try:
            product = get_cart_product(key)
            price = get_product_price(product)
            qty = int(item_data.get('qty', 1))
            total = price * qty
            cart_items.append({
                'key': key,
                'id': product.id,
                'name': get_product_name(product),
                'slug': get_product_slug(product),
                'image': get_product_image(product),
                'price': price,
                'qty': qty,
                'total': total,
            })
            subtotal += total
        except Exception:
            invalid_keys.append(key)

    for k in invalid_keys:
        del cart_data[k]
    if invalid_keys:
        request.session['cart'] = cart_data
        request.session.modified = True

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': 0.0,
        'total': subtotal,
        'item_count': sum(item['qty'] for item in cart_items),
    })


def checkout(request):
    cart_data = request.session.get('cart', {})
    cart_items = []
    subtotal = 0.0
    invalid_keys = []

    for key, item_data in cart_data.items():
        try:
            product = get_cart_product(key)
            price = get_product_price(product)
            qty = int(item_data.get('qty', 1))
            total = price * qty
            cart_items.append({
                'key': key,
                'id': product.id,
                'name': get_product_name(product),
                'slug': get_product_slug(product),
                'image': get_product_image(product),
                'price': price,
                'qty': qty,
                'total': total,
            })
            subtotal += total
        except Exception:
            invalid_keys.append(key)

    for k in invalid_keys:
        del cart_data[k]
    if invalid_keys:
        request.session['cart'] = cart_data
        request.session.modified = True

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': 0.0,
        'total': subtotal,
        'item_count': sum(item['qty'] for item in cart_items),
    })


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        cart_key = data.get('key', '')
        qty = int(data.get('qty', 1))
        if qty < 1:
            qty = 1

        try:
            product = get_cart_product(cart_key)
            price = get_product_price(product)
        except Exception:
            return JsonResponse({'success': False, 'message': 'Product not found.'})

        cart = request.session.get('cart', {})
        if cart_key in cart:
            cart[cart_key]['qty'] += qty
        else:
            cart[cart_key] = {'qty': qty}
        request.session['cart'] = cart
        request.session.modified = True

        item_count = sum(v['qty'] for v in cart.values())
        return JsonResponse({
            'success': True,
            'message': f'"{get_product_name(product)}" added to cart!',
            'item_count': item_count,
            'cart_total': sum(
                get_product_price(get_cart_product(k)) * v['qty']
                for k, v in cart.items()
            ),
        })
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        cart_key = data.get('key', '')
        qty = int(data.get('qty', 1))
        if qty < 1:
            qty = 1

        cart = request.session.get('cart', {})
        if cart_key in cart:
            cart[cart_key]['qty'] = qty
            request.session['cart'] = cart
            request.session.modified = True

            product = get_cart_product(cart_key)
            price = get_product_price(product)
            item_total = price * qty

            subtotal = sum(
                get_product_price(get_cart_product(k)) * v['qty']
                for k, v in cart.items()
            )
            item_count = sum(v['qty'] for v in cart.values())

            return JsonResponse({
                'success': True,
                'item_total': item_total,
                'subtotal': subtotal,
                'total': subtotal,
                'item_count': item_count,
            })
    return JsonResponse({'success': False})


@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        cart_key = data.get('key', '')

        cart = request.session.get('cart', {})
        if cart_key in cart:
            del cart[cart_key]
            request.session['cart'] = cart
            request.session.modified = True

        subtotal = sum(
            get_product_price(get_cart_product(k)) * v['qty']
            for k, v in cart.items()
        )
        item_count = sum(v['qty'] for v in cart.values())

        return JsonResponse({
            'success': True,
            'subtotal': subtotal,
            'total': subtotal,
            'item_count': item_count,
            'cart_empty': len(cart) == 0,
        })
    return JsonResponse({'success': False})


def payment(request):
    cart_data = request.session.get('cart', {})
    cart_items = []
    subtotal = 0.0
    invalid_keys = []

    for key, item_data in cart_data.items():
        try:
            product = get_cart_product(key)
            price = get_product_price(product)
            qty = int(item_data.get('qty', 1))
            total = price * qty
            cart_items.append({
                'key': key,
                'id': product.id,
                'name': get_product_name(product),
                'image': get_product_image(product),
                'price': price,
                'qty': qty,
                'total': total,
            })
            subtotal += total
        except Exception:
            invalid_keys.append(key)

    for k in invalid_keys:
        del cart_data[k]
    if invalid_keys:
        request.session['cart'] = cart_data
        request.session.modified = True

    return render(request, 'shop/payment.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': 0.0,
        'total': subtotal,
        'item_count': sum(item['qty'] for item in cart_items),
    })


def track_order(request):
    return render(request, 'shop/track_order.html')


@csrf_exempt
def newsletter_subscribe(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        email = data.get('email', '').strip()
        if not email:
            return JsonResponse({'success': False, 'message': 'Email is required.'})
        obj, created = NewsletterSubscription.objects.get_or_create(
            email=email,
            defaults={'is_active': True}
        )
        if created:
            return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})
        else:
            return JsonResponse({'success': True, 'message': 'You are already subscribed!'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


def login_view(request):
    illustrations = LoginIllustration.objects.filter(is_active=True).order_by('order')
    return render(request, 'shop/login.html', {'login_illustrations': illustrations})
