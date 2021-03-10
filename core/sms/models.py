from django.db import models
from django.utils.translation import ugettext_lazy as _
from random import randint


class AuthSms(models.Model):
    phone_number = models.CharField(verbose_name=_('휴대폰번호'), max_length=11, primary_key=True)
    auth_number = models.IntegerField(verbose_name=_('인증번호'), blank=True)

    created_at = models.DateTimeField(verbose_name=_('생성날짜'), auto_now_add=True)

    class Meta:
        db_table = 'auth_numbers'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.auth_number:
            while True:
                self.auth_number: int = randint(1000, 9999)
                break

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.phone_number} / {self.auth_number}'
