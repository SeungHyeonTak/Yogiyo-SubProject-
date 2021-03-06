# Generated by Django 3.1.4 on 2021-01-03 16:04

import app.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=15, verbose_name='License Number')),
                ('license_copy', models.ImageField(upload_to=app.models.get_license_copy_path, verbose_name='License Copy')),
                ('report', models.ImageField(upload_to=app.models.get_business_report_path, verbose_name='Report')),
                ('business_name', models.CharField(max_length=25, verbose_name='Business Name')),
                ('business_phone', models.CharField(max_length=20, verbose_name='Business Phone')),
                ('restaurant_name', models.CharField(max_length=25, verbose_name='Restaurant Name')),
                ('restaurant_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Restaurant Phone')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('delivery', models.IntegerField(choices=[(0, '배달만 가능'), (1, '배달 + 테이크아웃 가능')], verbose_name='Delivery')),
                ('leaflet', models.ImageField(blank=True, null=True, upload_to=app.models.get_leaflet_path, verbose_name='Leaflet')),
                ('is_check', models.BooleanField(default=False, verbose_name='is check')),
                ('reason', models.TextField(blank=True, null=True, verbose_name='Reason')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'application_form',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BundleMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bundlemenu',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BundleOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('price', models.CharField(max_length=25, verbose_name='Price')),
                ('is_essential', models.BooleanField(default=False, verbose_name='is essential')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bundle_option',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'category',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Payment Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'payment_type',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_order', models.CharField(default='0', max_length=20, verbose_name='Minimum Order')),
                ('delivery_charges', models.CharField(default='0', max_length=20, verbose_name='Delivery Charges')),
                ('owner_notice', models.TextField(blank=True, null=True, verbose_name='Owner Notice')),
                ('grade', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Grade')),
                ('business_hours', models.CharField(blank=True, max_length=50, null=True, verbose_name='Business Hours')),
                ('origin', models.TextField(blank=True, null=True, verbose_name='Origin')),
                ('is_application_form', models.BooleanField(default=False, verbose_name='Application Form')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('application_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_forms', to='app.applicationform')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_types', to='app.paymenttype')),
            ],
            options={
                'db_table': 'restaurant',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('price', models.CharField(max_length=30, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('bundle_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundle_options', to='app.bundleoption')),
            ],
            options={
                'db_table': 'option',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('explanation', models.CharField(blank=True, max_length=255, null=True, verbose_name='Explanation')),
                ('price', models.CharField(max_length=25, verbose_name='Price')),
                ('food_image', models.ImageField(blank=True, null=True, upload_to=app.models.get_food_image_path, verbose_name='Food Image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('bundle_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundlemenus', to='app.bundlemenu')),
            ],
            options={
                'db_table': 'menu',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='bundleoption',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='app.menu'),
        ),
        migrations.AddField(
            model_name='bundlemenu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='app.restaurant'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorys', to='app.category'),
        ),
    ]
