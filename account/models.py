from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _  # 다국어 지원
from app.models import Restaurant


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError(_('User must have an email address'))

        # text) self.model() -> 저장되지 않은 인스턴스 모델?
        user = self.model(
            # text) normalize_email : @도메인에 대한 정규화만 진행 / 정규화는 곧 소문자화
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        # text) self._db의 의미 -> settings.py의 DATABASES 안에 default로 쓰이는 DB를 가리킨다.
        # text) 또한 다른 DB를 사용하고 싶다면 해당 딕셔너리의 이름을 사용하면된다. ex) using='prod_server'
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
        )

        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name=_('Email address'), max_length=255, unique=True)
    nickname = models.CharField(verbose_name=_('NickName'), max_length=30, unique=True, blank=True, null=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=20)

    is_active = models.BooleanField(verbose_name=_('is active'), default=False)
    is_withdrawal = models.BooleanField(verbose_name=_('is withdrawal'), default=False)
    is_superuser = models.BooleanField(verbose_name=_('is superuser'), default=False)

    date_joined = models.DateTimeField(verbose_name=_('date joined'), auto_now_add=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', ]

    class Meta:
        db_table = 'auth_user'
        ordering = ['-created_at']
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.nickname

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Owner(models.Model):
    """created_at 추가 및 Meta Class 추가하기"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    name = models.CharField(verbose_name=_('Name'), max_length=10)
    personal_phone = models.CharField(verbose_name=_('Personal Phone'), max_length=20)

    is_register = models.BooleanField(verbose_name=_('is register'), default=False)
    is_cancel = models.BooleanField(verbose_name=_('is cancel'), default=False)

    reason = models.CharField(verbose_name=_('Reason'), max_length=255, blank=True, null=True)
