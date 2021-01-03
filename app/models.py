import time
from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _


def get_license_copy_path(instance, filename):
    return f'license/copy' \
           f'/{instance.pk if instance.pk else int(time.time())}_{uuid4().hex}.' \
           f'{filename(".")[-1] if filename.split(".") else "jpg"}'


def get_business_report_path(instance, filename):
    return f'business/report/' \
           f'{instance.pk if instance.pk else int(time.time())}_{uuid4().hex}.' \
           f'{filename(".")[-1] if filename.split(".") else "jpg"}'


def get_leaflet_path(instance, filename):
    return f'leaflet/' \
           f'{instance.pk if instance.pk else int(time.time())}_{uuid4().hex}.' \
           f'{filename(".")[-1] if filename.split(".") else "jpg"}'


def get_food_image_path(instance, filename):
    return f'food/{instance.pk if instance.pk else int(time.time())}_' \
           f'{uuid4().hex}.{filename(".")[-1] if filename.split(".") else "jpg"}'


class Category(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class PaymentType(models.Model):
    """
    결제 타입:
    app_pay : 요기서결제
    meet_pay : 현장결제(현금/카드)
    one_second_pay : 요기서 1초결제
    """
    name = models.CharField(verbose_name=_('Payment Name'), max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payment_type'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class ApplicationForm(models.Model):
    """
    입점신청서
    """
    ONLY_DELIVERY, DELIVERY_TAKE = 0, 1
    DELIVERY_CHOICE = (
        (ONLY_DELIVERY, '배달만 가능'),
        (DELIVERY_TAKE, '배달 + 테이크아웃 가능'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')

    license_number = models.CharField(verbose_name=_('License Number'), max_length=15)
    license_copy = models.ImageField(verbose_name=_('License Copy'), upload_to=get_license_copy_path)  # 사업자등록증 사본
    report = models.ImageField(verbose_name=_('Report'), upload_to=get_business_report_path)  # 영업신고증 사본
    business_name = models.CharField(verbose_name=_('Business Name'), max_length=25)
    business_phone = models.CharField(verbose_name=_('Business Phone'), max_length=20)

    restaurant_name = models.CharField(verbose_name=_('Restaurant Name'), max_length=25)
    restaurant_phone = models.CharField(verbose_name=_('Restaurant Phone'), max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name=_('Address'), max_length=255)
    delivery = models.IntegerField(verbose_name=_('Delivery'), choices=DELIVERY_CHOICE)
    leaflet = models.ImageField(verbose_name=_('Leaflet'), upload_to=get_leaflet_path, blank=True, null=True)
    is_check = models.BooleanField(verbose_name=_('is check'), default=False)  # 입점신청 확인 체크
    reason = models.TextField(verbose_name=_('Reason'), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'application_form'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.restaurant_name}'


class Restaurant(models.Model):
    """
    가게 (입점신청이 완료되야함)
    """
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, related_name='payment_types')
    application_form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name='application_forms')

    minimum_order = models.CharField(verbose_name=_('Minimum Order'), max_length=20, default='0')  # 최소 주문 금액
    delivery_charges = models.CharField(verbose_name=_('Delivery Charges'), max_length=20, default='0')  # 배달료
    owner_notice = models.TextField(verbose_name=_('Owner Notice'), blank=True, null=True)  # 사장님 알림(공지)
    grade = models.IntegerField(
        verbose_name=_('Grade'), validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True
    )  # 별점
    business_hours = models.CharField(verbose_name=_('Business Hours'), max_length=50, blank=True, null=True)  # 영업시간
    origin = models.TextField(verbose_name=_('Origin'), blank=True, null=True)  # 원산지
    is_application_form = models.BooleanField(verbose_name=_('Application Form'), default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'restaurant'
        ordering = ['-created_at']


class BundleMenu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bundlemenu'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class Menu(models.Model):
    bundle_menu = models.ForeignKey(BundleMenu, on_delete=models.CASCADE, related_name='bundlemenus')

    name = models.CharField(verbose_name=_('Name'), max_length=25)
    explanation = models.CharField(verbose_name=_('Explanation'), max_length=255, blank=True, null=True)
    price = models.CharField(verbose_name=_('Price'), max_length=25)
    food_image = models.ImageField(verbose_name=_('Food Image'), upload_to=get_food_image_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'menu'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class BundleOption(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menus')

    name = models.CharField(verbose_name=_('Name'), max_length=25)

    is_essential = models.BooleanField(verbose_name=_('is essential'), default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bundle_option'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class Option(models.Model):
    bundle_option = models.ForeignKey(BundleOption, on_delete=models.CASCADE, related_name='bundle_options')

    name = models.CharField(verbose_name=_('Name'), max_length=30)
    price = models.CharField(verbose_name=_('Price'), max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'option'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    """주문"""
    pass


class Payment(models.Model):
    """결제"""
    pass
