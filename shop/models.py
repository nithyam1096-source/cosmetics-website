from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, verbose_name='Category Name')
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    button_text = models.CharField(max_length=50, default='Shop Now')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200, default='', blank=True)
    description = models.TextField()
    short_description = models.TextField(blank=True, help_text='Leave empty for auto-generated beauty description')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    category_tag = models.CharField(max_length=50, default='New', choices=[
        ('New', 'New'),
        ('Best Seller', 'Best Seller'),
        ('Trending', 'Trending'),
        ('Limited', 'Limited Edition'),
    ])
    rating = models.PositiveIntegerField(default=4, choices=[(i, str(i)) for i in range(1, 6)])
    reviews = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.title or not self.title.strip():
            self.title = self.name
        if not self.short_description or not self.short_description.strip():
            self.short_description = self._generate_description()
        super().save(*args, **kwargs)

    def _generate_description(self):
        name_lower = self.name.lower()
        if 'lipstick' in name_lower:
            return "Ultra-smooth matte finish with 12-hour long wear."
        elif 'serum' in name_lower:
            return "Brightens skin and boosts natural glow."
        elif 'foundation' in name_lower:
            return "Lightweight coverage with flawless finish."
        elif 'mascara' in name_lower:
            return "Volumizing formula for dramatic, lash-defining effects."
        elif 'blush' in name_lower:
            return "Silky powder that delivers a natural, rosy flush."
        elif 'primer' in name_lower:
            return "Smooth, poreless base for long-lasting makeup."
        elif 'moisturizer' in name_lower:
            return "Deep hydration for 24-hour radiant, dewy skin."
        elif 'cleanser' in name_lower:
            return "Gentle, foaming formula that purifies without stripping."
        elif 'eyeshadow' in name_lower:
            return "Highly pigmented blend for captivating, long-lasting looks."
        elif 'toner' in name_lower:
            return "Balancing formula that refines and preps your skin."
        return "Premium beauty product crafted for exceptional results."

    @property
    def discount_percentage(self):
        if self.discount_price and self.price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, default='Shop Now')
    button_url = models.CharField(max_length=200, default='/shop')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Banner #{self.order}'


class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    discount_percentage = models.PositiveIntegerField()
    expiry_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-expiry_date']

    def __str__(self):
        return self.title

    @property
    def is_expired(self):
        return timezone.now() > self.expiry_date


class AboutSection(models.Model):
    heading = models.CharField(max_length=250, default='Where Luxury Meets Skin Science')
    description = models.TextField(default='Discover the art of premium skincare with our meticulously crafted collection. Each product combines advanced dermatological science with luxurious botanical ingredients, delivering visible results that transform your daily routine into an indulgent beauty ritual.')
    main_image = models.ImageField(upload_to='about/', blank=True, null=True)
    overlap_image = models.ImageField(upload_to='about/', blank=True, null=True)
    animation_enabled = models.BooleanField(default=True, help_text='Enable floating and fade-in animations')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'

    def __str__(self):
        return self.heading


class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='ingredients/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.title


class WhyGlowifySection(models.Model):
    heading = models.CharField(max_length=200, default='Why Glowify')
    subheading = models.CharField(max_length=300, default='Premium skincare crafted for radiant beauty and confidence.')
    model_image = models.ImageField(upload_to='whyglowify/', blank=True, null=True, help_text='Upload a beauty model image')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Why Glowify Section'
        verbose_name_plural = 'Why Glowify Sections'
        ordering = ['-created_at']

    def __str__(self):
        return self.heading


class WhyGlowifyFeature(models.Model):
    section = models.ForeignKey(WhyGlowifySection, on_delete=models.CASCADE, related_name='features')
    number = models.CharField(max_length=4, help_text='e.g. 01, 02, 03, 04')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text='Short description for this feature')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Why Glowify Feature'
        verbose_name_plural = 'Why Glowify Features'
        ordering = ['order']

    def __str__(self):
        return f'{self.number} - {self.title}'


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.name}, {self.city}'


class FlashSaleBanner(models.Model):
    model_image = models.ImageField(upload_to='flash_sale/', blank=True, null=True, help_text='Upload anime-style beauty girl illustration (left side)')
    product_image = models.ImageField(upload_to='flash_sale/', blank=True, null=True, help_text='Upload product image (right side)')

    subheading = models.CharField(max_length=300, blank=True, default='Premium beauty essentials for your daily glow')
    sale_percentage = models.CharField(max_length=10, default='50%')
    heading = models.CharField(max_length=200, default='Glow Confidently every Day')
    button_text = models.CharField(max_length=50, default='Shop Now')
    button_url = models.CharField(max_length=500, default='/shop/')

    semi_circle_color_start = models.CharField(max_length=20, default='#FFE4E1', help_text='Semicircle gradient start color (soft blush)')
    semi_circle_color_end = models.CharField(max_length=20, default='#FF69B4', help_text='Semicircle gradient end color (bright pink)')

    enable_sparkles = models.BooleanField(default=True, help_text='Enable sparkle/glow particles around cream jar')
    enable_particles = models.BooleanField(default=True, help_text='Enable floating background particles')
    enable_countdown = models.BooleanField(default=False, help_text='Show countdown timer')
    countdown_end = models.DateTimeField(blank=True, null=True)

    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Flash Sale Banner'
        verbose_name_plural = 'Flash Sale Banners'

    def __str__(self):
        return f'Flash Sale - {self.sale_percentage} Off'


class FooterSettings(models.Model):
    background_image = models.ImageField(upload_to='footer/', blank=True, null=True, help_text='Upload footer background image')
    bg_color_start = models.CharField(max_length=20, default='#ff4fa3', help_text='Footer gradient start color')
    bg_color_end = models.CharField(max_length=20, default='#ff1493', help_text='Footer gradient end color')

    logo_text = models.CharField(max_length=50, default='Glowify', help_text='Brand logo text')
    address = models.TextField(default='3rd Floor, Valasaravakam,\nChennai - 600800', help_text='Footer address')

    quick_link_1_text = models.CharField(max_length=50, default='Shop')
    quick_link_1_url = models.CharField(max_length=200, default='/shop/')
    quick_link_2_text = models.CharField(max_length=50, default='New Arrivals')
    quick_link_2_url = models.CharField(max_length=200, default='/shop/?sort=newest')
    quick_link_3_text = models.CharField(max_length=50, default='Offers')
    quick_link_3_url = models.CharField(max_length=200, default='/offers/')

    support_link_1_text = models.CharField(max_length=50, default='About')
    support_link_1_url = models.CharField(max_length=200, default='/about/')
    support_link_2_text = models.CharField(max_length=50, default='Contact')
    support_link_2_url = models.CharField(max_length=200, default='/contact/')
    support_link_3_text = models.CharField(max_length=50, default='Terms & Conditions')
    support_link_3_url = models.CharField(max_length=200, default='#')
    support_link_4_text = models.CharField(max_length=50, default='Privacy Policy')
    support_link_4_url = models.CharField(max_length=200, default='#')

    facebook_url = models.CharField(max_length=200, default='#', blank=True, help_text='Facebook page URL')
    instagram_url = models.CharField(max_length=200, default='#', blank=True, help_text='Instagram page URL')

    copyright_text = models.CharField(max_length=200, default='© 2026 Glowify. All rights reserved.')

    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Footer Setting'
        verbose_name_plural = 'Footer Settings'

    def __str__(self):
        return 'Footer Settings'


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = 'Newsletter Subscription'
        verbose_name_plural = 'Newsletter Subscriptions'

    def __str__(self):
        return self.email


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class EyeMakeupProduct(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='eye_makeup_products')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='eye_makeup/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.PositiveIntegerField(default=4, choices=[(i, i) for i in range(1, 6)])
    reviews = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Eye Makeup Product'
        verbose_name_plural = 'Eye Makeup Products'

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        if self.discount_price and self.price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price


class FragranceProduct(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='fragrance_products')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='fragrance/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.PositiveIntegerField(default=4, choices=[(i, i) for i in range(1, 6)])
    reviews = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Fragrance Product'
        verbose_name_plural = 'Fragrance Products'

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        if self.discount_price and self.price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price


class HairCareProduct(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='hair_care_products')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hair_care/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.PositiveIntegerField(default=4, choices=[(i, i) for i in range(1, 6)])
    reviews = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Hair Care Product'
        verbose_name_plural = 'Hair Care Products'

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        if self.discount_price and self.price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price


class LipstickProduct(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='lipstick_products')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='lipsticks/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.PositiveIntegerField(default=4, choices=[(i, i) for i in range(1, 6)])
    reviews = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Lipstick Product'
        verbose_name_plural = 'Lipstick Products'

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        if self.discount_price and self.price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price


class NailProduct(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='nail_products')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='nails/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rating = models.PositiveIntegerField(default=4, choices=[(i, i) for i in range(1, 6)])
    reviews = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Nail Product'
        verbose_name_plural = 'Nail Products'

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        if self.discount_price and self.price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price


class OfferBanner(models.Model):
    image = models.ImageField(upload_to='offers/', blank=True, null=True, help_text='Upload offers page banner image (1920x700 recommended)')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Offer Banner'
        verbose_name_plural = 'Offer Banners'

    def __str__(self):
        return f'Offer Banner #{self.order}'


class OfferProduct(models.Model):
    image = models.ImageField(upload_to='offer_products/')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Offer Product'
        verbose_name_plural = 'Offer Products'

    def __str__(self):
        return self.title


class MidnightSet(models.Model):
    image = models.ImageField(upload_to='midnight_set/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Midnight Set'
        verbose_name_plural = 'Midnight Sets'

    def __str__(self):
        return 'Midnight Repair Set'


class NewsletterImage(models.Model):
    image = models.ImageField(upload_to='newsletter/', help_text='Upload newsletter left side image')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Newsletter Image'
        verbose_name_plural = 'Newsletter Images'

    def __str__(self):
        return 'Newsletter Image'


class AboutHeroBanner(models.Model):
    background_image = models.ImageField(upload_to='about_hero/', help_text='Upload background image for the hero banner')
    title = models.CharField(max_length=200, default='The Art of Radiant Skin')
    subtitle = models.TextField(default='The legacy of timeless beauty and scientific precision, crafted for the modern connoisseur')
    button_text = models.CharField(max_length=100, default='Explore Collection')
    button_url = models.CharField(max_length=500, default='#', blank=True)
    overlay_opacity = models.DecimalField(max_digits=3, decimal_places=2, default=0.15, help_text='Overlay opacity (0.00 to 1.00)')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Hero Banner'
        verbose_name_plural = 'About Hero Banners'

    def __str__(self):
        return 'About Hero Banner'


class AboutRightImage(models.Model):
    image = models.ImageField(upload_to='about_right/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'About Right Image'
        verbose_name_plural = 'About Right Images'
        ordering = ['order']

    def __str__(self):
        return self.caption or f'Image {self.order}'


class FounderSection(models.Model):
    image = models.ImageField(upload_to='founder/', help_text='Upload founder portrait image')
    name = models.CharField(max_length=100, default='Elena')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Founder Section'
        verbose_name_plural = 'Founder Sections'
        ordering = ['-created_at']

    def __str__(self):
        return f'Founder: {self.name}'


class ContactBanner(models.Model):
    background_image = models.ImageField(upload_to='contact_banner/', help_text='Upload contact banner background image (1920x500 recommended)')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Banner'
        verbose_name_plural = 'Contact Banners'
        ordering = ['-created_at']

    def __str__(self):
        return 'Contact Banner'


class LoginIllustration(models.Model):
    image = models.ImageField(upload_to='login/', help_text='Upload illustration image for login page left side')
    caption = models.CharField(max_length=200, blank=True, default='')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Login Illustration'
        verbose_name_plural = 'Login Illustrations'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.caption or f'Login Illustration #{self.pk}'
