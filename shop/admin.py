from django.contrib import admin
from .models import Category, Product, Banner, Offer, AboutSection, Ingredient, WhyGlowifySection, WhyGlowifyFeature, Testimonial, FlashSaleBanner, FooterSettings, NewsletterSubscription, Brand, EyeMakeupProduct, FragranceProduct, HairCareProduct, LipstickProduct, NailProduct, OfferBanner, OfferProduct, MidnightSet, NewsletterImage, AboutHeroBanner, AboutRightImage, FounderSection, ContactBanner, LoginIllustration


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'subtitle', 'image_preview', 'button_text', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('category_name', 'subtitle', 'description')
    prepopulated_fields = {'slug': ('category_name',)}
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_large',)
    fields = ('category_name', 'slug', 'subtitle', 'description', 'image', 'image_preview_large', 'button_text', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 12px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 300px; border-radius: 16px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Image Preview'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_tag', 'price', 'rating', 'reviews', 'is_featured', 'is_active', 'created_at')
    list_filter = ('is_active', 'is_featured', 'category_tag')
    search_fields = ('name', 'description', 'short_description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'is_featured', 'is_active', 'category_tag')
    readonly_fields = ('image_preview_large',)
    fields = ('name', 'slug', 'title', 'description', 'short_description', 'image', 'image_preview_large', 'price', 'discount_price', 'category_tag', 'rating', 'reviews', 'stock', 'category', 'is_featured', 'is_active')

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 300px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);" />')
        return "No image"
    image_preview_large.short_description = 'Image Preview'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'button_text', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    readonly_fields = ('image_preview_large',)
    fields = ('image', 'image_preview_large', 'button_text', 'button_url', 'order', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 6px;" />')
        return "No image"
    image_preview.short_description = 'Preview'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 400px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Image Preview'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('image_preview_large',)
    fields = ('title', 'description', 'image', 'image_preview_large')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 250px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);" />')
        return "No image"
    image_preview_large.short_description = 'Preview'


@admin.register(HairCareProduct)
class HairCareProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discount_price', 'rating', 'stock', 'image_preview', 'is_active', 'created_at')
    list_filter = ('is_active', 'brand')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'discount_price', 'is_active')
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'brand', 'description'),
        }),
        ('Media', {
            'fields': ('image', 'image_preview_large'),
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price', 'stock'),
        }),
        ('Ratings', {
            'fields': ('rating', 'reviews'),
        }),
        ('Settings', {
            'fields': ('is_active',),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 250px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);" />')
        return "No image"
    image_preview_large.short_description = 'Preview'


@admin.register(LipstickProduct)
class LipstickProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discount_price', 'rating', 'stock', 'image_preview', 'is_active', 'created_at')
    list_filter = ('is_active', 'brand')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'discount_price', 'is_active')
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'brand', 'description'),
        }),
        ('Media', {
            'fields': ('image', 'image_preview_large'),
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price', 'stock'),
        }),
        ('Ratings', {
            'fields': ('rating', 'reviews'),
        }),
        ('Settings', {
            'fields': ('is_active',),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 250px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);" />')
        return "No image"
    image_preview_large.short_description = 'Preview'


@admin.register(NailProduct)
class NailProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discount_price', 'rating', 'stock', 'image_preview', 'is_active', 'created_at')
    list_filter = ('is_active', 'brand')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'discount_price', 'is_active')
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'brand', 'description'),
        }),
        ('Media', {
            'fields': ('image', 'image_preview_large'),
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price', 'stock'),
        }),
        ('Ratings', {
            'fields': ('rating', 'reviews'),
        }),
        ('Settings', {
            'fields': ('is_active',),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 250px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);" />')
        return "No image"
    image_preview_large.short_description = 'Preview'




@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount_percentage', 'expiry_date', 'is_active', 'is_expired')
    list_filter = ('is_active',)
    search_fields = ('title',)

    def is_expired(self, obj):
        return obj.is_expired
    is_expired.boolean = True
    is_expired.short_description = 'Expired'


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('heading_preview', 'image_preview', 'animation_enabled', 'is_active', 'updated_at')
    list_filter = ('is_active', 'animation_enabled')
    search_fields = ('heading', 'description')
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_panel',)
    fieldsets = (
        ('Content', {
            'fields': ('heading', 'description'),
        }),
        ('Images', {
            'fields': ('main_image', 'overlap_image', 'image_preview_panel'),
        }),
        ('Settings', {
            'fields': ('animation_enabled', 'is_active'),
            'classes': ('collapse',),
        }),
    )

    def heading_preview(self, obj):
        text = obj.heading or 'About Section'
        return (text[:50] + '...') if len(text) > 50 else text
    heading_preview.short_description = 'Heading'

    def image_preview(self, obj):
        if obj.main_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.main_image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px; border: 1px solid #e0e0e0;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_panel(self, obj):
        from django.utils.safestring import mark_safe
        html = '<div style="display: flex; gap: 25px; flex-wrap: wrap; align-items: flex-end;">'
        if obj.main_image:
            html += f'<div style="text-align: center;"><p style="margin: 0 0 10px 0; font-weight: 600; font-size: 0.85rem; color: #555; text-transform: uppercase; letter-spacing: 1px;">Main Image</p><img src="{obj.main_image.url}" style="max-width: 300px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);" /></div>'
        if obj.overlap_image:
            html += f'<div style="text-align: center;"><p style="margin: 0 0 10px 0; font-weight: 600; font-size: 0.85rem; color: #555; text-transform: uppercase; letter-spacing: 1px;">Overlap Image</p><img src="{obj.overlap_image.url}" style="max-width: 220px; border-radius: 14px; box-shadow: 0 10px 30px rgba(255,105,180,0.15); margin-top: 25px;" /></div>'
        html += '</div>'
        return mark_safe(html) if obj.main_image or obj.overlap_image else mark_safe('<p style="color: #999;">No images uploaded yet</p>')
    image_preview_panel.short_description = 'Image Previews'


@admin.register(WhyGlowifySection)
class WhyGlowifySectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'image_preview', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('heading', 'subheading')
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Content', {
            'fields': ('heading', 'subheading'),
        }),
        ('Image', {
            'fields': ('model_image', 'image_preview_large'),
        }),
        ('Settings', {
            'fields': ('is_active',),
            'classes': ('collapse',),
        }),
    )

    def image_preview(self, obj):
        if obj.model_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.model_image.url}" style="width: 50px; height: 60px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.model_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.model_image.url}" style="max-width: 300px; border-radius: 16px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Preview'


@admin.register(WhyGlowifyFeature)
class WhyGlowifyFeatureAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'section', 'order', 'is_active')
    list_filter = ('is_active', 'section')
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')
    list_display_links = ('number', 'title')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'city', 'rating', 'order', 'is_active')
    list_filter = ('is_active', 'rating')
    search_fields = ('name', 'city', 'review_text')
    list_editable = ('order', 'is_active')
    readonly_fields = ('image_preview_large',)
    fields = ('name', 'city', 'image', 'image_preview_large', 'review_text', 'rating', 'order', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; border: 2px solid #FF69B4;" />')
        return "—"
    image_preview.short_description = 'Photo'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 200px; border-radius: 50%; border: 4px solid #FF69B4; box-shadow: 0 5px 20px rgba(255,105,180,0.3);" />')
        return "No image"
    image_preview_large.short_description = 'Photo Preview'


@admin.register(FlashSaleBanner)
class FlashSaleBannerAdmin(admin.ModelAdmin):
    list_display = ('sale_percentage', 'heading_preview', 'image_preview', 'is_active', 'start_time', 'end_time')
    list_filter = ('is_active',)
    search_fields = ('heading',)
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_large', 'product_preview')
    fieldsets = (
        ('Left Side - Model Image', {
            'fields': ('model_image', 'image_preview_large'),
        }),
        ('Right Side - Product Image', {
            'fields': ('product_image', 'product_preview'),
        }),
        ('Content', {
            'fields': ('sale_percentage', 'heading', 'subheading', 'button_text', 'button_url'),
        }),
        ('Semicircle Background', {
            'fields': ('semi_circle_color_start', 'semi_circle_color_end'),
            'description': 'Customize the large semicircle gradient colors at the center of the banner.',
        }),
        ('Settings', {
            'fields': ('enable_sparkles', 'enable_particles', 'enable_countdown', 'countdown_end', 'start_time', 'end_time', 'is_active'),
            'classes': ('collapse',),
        }),
    )

    def heading_preview(self, obj):
        text = obj.heading or 'Flash Sale'
        return (text[:60] + '...') if len(text) > 60 else text
    heading_preview.short_description = 'Heading'

    def image_preview(self, obj):
        if obj.model_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.model_image.url}" style="width: 40px; height: 50px; object-fit: cover; border-radius: 6px;" />')
        return "—"
    image_preview.short_description = 'Model'

    def image_preview_large(self, obj):
        if obj.model_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.model_image.url}" style="max-width: 250px; border-radius: 16px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Model Preview'

    def product_preview(self, obj):
        if obj.product_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.product_image.url}" style="max-width: 120px; border-radius: 12px; box-shadow: 0 3px 10px rgba(0,0,0,0.08);" />')
        return "—"
    product_preview.short_description = 'Preview'


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email',)
    list_editable = ('is_active',)
    readonly_fields = ('subscribed_at',)


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ('logo_text', 'image_preview', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_large', 'updated_at')
    fieldsets = (
        ('Background', {
            'fields': ('background_image', 'image_preview_large', 'bg_color_start', 'bg_color_end'),
        }),
        ('Brand', {
            'fields': ('logo_text', 'address', 'copyright_text'),
        }),
        ('Quick Links', {
            'fields': (
                ('quick_link_1_text', 'quick_link_1_url'),
                ('quick_link_2_text', 'quick_link_2_url'),
                ('quick_link_3_text', 'quick_link_3_url'),
            ),
        }),
        ('Support Links', {
            'fields': (
                ('support_link_1_text', 'support_link_1_url'),
                ('support_link_2_text', 'support_link_2_url'),
                ('support_link_3_text', 'support_link_3_url'),
                ('support_link_4_text', 'support_link_4_url'),
            ),
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url'),
        }),
        ('Settings', {
            'fields': ('is_active', 'updated_at'),
        }),
    )

    def image_preview(self, obj):
        if obj.background_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.background_image.url}" style="width: 60px; height: 40px; object-fit: cover; border-radius: 6px;" />')
        return "—"
    image_preview.short_description = 'BG'

    def image_preview_large(self, obj):
        if obj.background_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.background_image.url}" style="max-width: 500px; width: 100%; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.15);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Background Preview'


@admin.register(LoginIllustration)
class LoginIllustrationAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image_preview', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('caption',)
    readonly_fields = ('image_preview_large', 'created_at')
    fields = ('image', 'image_preview_large', 'caption', 'order', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 12px;" />')
        return "—"
    image_preview.short_description = 'Preview'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 400px; width: 100%; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.15);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Image Preview'


@admin.register(OfferBanner)
class OfferBannerAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'order', 'is_active', 'created_at')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 80px; height: 45px; object-fit: cover; border-radius: 6px;" />')
        return "—"
    image_preview.short_description = 'Preview'


@admin.register(OfferProduct)
class OfferProductAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'discount_price', 'original_price', 'order', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'


@admin.register(MidnightSet)
class MidnightSetAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'is_active', 'created_at')
    list_filter = ('is_active',)

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 12px;" />')
        return "—"
    image_preview.short_description = 'Image'


@admin.register(NewsletterImage)
class NewsletterImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'is_active')
    list_filter = ('is_active',)

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 80px; height: 50px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Preview'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('name',)


@admin.register(EyeMakeupProduct)
class EyeMakeupProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discount_price', 'rating', 'stock', 'image_preview', 'is_active', 'created_at')
    list_filter = ('is_active', 'brand')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'discount_price', 'is_active')
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'brand', 'description'),
        }),
        ('Media', {
            'fields': ('image', 'image_preview_large'),
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price', 'stock'),
        }),
        ('Ratings', {
            'fields': ('rating', 'reviews'),
        }),
        ('Settings', {
            'fields': ('is_active',),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 250px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);" />')
        return "No image"
    image_preview_large.short_description = 'Preview'


@admin.register(FragranceProduct)
class FragranceProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'discount_price', 'rating', 'stock', 'image_preview', 'is_active', 'created_at')
    list_filter = ('is_active', 'brand')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'discount_price', 'is_active')
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'brand', 'description'),
        }),
        ('Media', {
            'fields': ('image', 'image_preview_large'),
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price', 'stock'),
        }),
        ('Ratings', {
            'fields': ('rating', 'reviews'),
        }),
        ('Settings', {
            'fields': ('is_active',),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 250px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1);" />')
        return "No image"
    image_preview_large.short_description = 'Preview'


@admin.register(AboutHeroBanner)
class AboutHeroBannerAdmin(admin.ModelAdmin):
    list_display = ('title_preview', 'image_preview', 'overlay_opacity', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_large',)
    fieldsets = (
        ('Background Image', {
            'fields': ('background_image', 'image_preview_large'),
        }),
        ('Content', {
            'fields': ('title', 'subtitle', 'button_text', 'button_url'),
        }),
        ('Settings', {
            'fields': ('overlay_opacity', 'is_active'),
            'classes': ('collapse',),
        }),
    )

    def title_preview(self, obj):
        text = obj.title or 'Hero Banner'
        return (text[:50] + '...') if len(text) > 50 else text
    title_preview.short_description = 'Title'

    def image_preview(self, obj):
        if obj.background_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.background_image.url}" style="width: 80px; height: 50px; object-fit: cover; border-radius: 6px;" />')
        return "—"
    image_preview.short_description = 'BG'

    def image_preview_large(self, obj):
        if obj.background_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.background_image.url}" style="max-width: 500px; width: 100%; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.15);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Background Preview'


@admin.register(AboutRightImage)
class AboutRightImageAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'caption', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('image_preview_large',)
    fields = ('image', 'image_preview_large', 'caption', 'order', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 300px; border-radius: 14px; box-shadow: 0 8px 25px rgba(0,0,0,0.1);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Preview'


@admin.register(FounderSection)
class FounderSectionAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_large',)
    fields = ('image', 'image_preview_large', 'name', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 60px; object-fit: cover; border-radius: 8px;" />')
        return "—"
    image_preview.short_description = 'Photo'

    def image_preview_large(self, obj):
        if obj.image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="max-width: 350px; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Preview'


@admin.register(ContactBanner)
class ContactBannerAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    readonly_fields = ('image_preview_large',)
    fields = ('background_image', 'image_preview_large', 'is_active')

    def image_preview(self, obj):
        if obj.background_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.background_image.url}" style="width: 80px; height: 50px; object-fit: cover; border-radius: 6px;" />')
        return "—"
    image_preview.short_description = 'Preview'

    def image_preview_large(self, obj):
        if obj.background_image:
            from django.utils.safestring import mark_safe
            return mark_safe(f'<img src="{obj.background_image.url}" style="max-width: 500px; width: 100%; border-radius: 16px; box-shadow: 0 10px 40px rgba(0,0,0,0.15);" />')
        return "No image uploaded"
    image_preview_large.short_description = 'Background Preview'
