# Generated by Django 3.1.4 on 2021-03-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_applicationform_final_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='final_confirmation',
            field=models.BooleanField(default=False, verbose_name='입점 신청서 제출 확인'),
        ),
    ]
