from .models import FooterSettings, Category, NewsletterImage


def footer_settings(request):
    try:
        footer = FooterSettings.objects.filter(is_active=True).first()
    except Exception:
        footer = None
    return {'footer_settings': footer}


def navbar_categories(request):
    try:
        categories = Category.objects.filter(is_active=True)
    except Exception:
        categories = []
    return {'navbar_categories': categories}


def newsletter_image(request):
    try:
        img = NewsletterImage.objects.filter(is_active=True).first()
    except Exception:
        img = None
    return {'newsletter_img': img}


def cart_count(request):
    cart = request.session.get('cart', {})
    count = sum(v.get('qty', 0) for v in cart.values())
    return {'cart_count': count}
