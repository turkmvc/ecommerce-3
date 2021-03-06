# Generated by Django 2.0 on 2019-01-14 22:07

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminGorevler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Dil',
                'verbose_name_plural': 'Dil Yönetimi',
            },
        ),
        migrations.CreateModel(
            name='Moduller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.PositiveSmallIntegerField(choices=[(1, 'Banner Yönetimi'), (2, 'Foto Galeri Yönetimi'), (3, 'Haber Yönetimi'), (4, 'İçerik  Yönetimi'), (5, 'Ürün Yönetimi'), (6, 'Referans Yönetimi'), (7, 'Video Galeri Yönetimi')], verbose_name='Modül Adı')),
                ('banner', models.CharField(help_text='Banner boyutlarını 600x400 şeklinde giriniz.', max_length=50, verbose_name='Fotoğraf boyutları')),
                ('durum', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Modül',
                'verbose_name_plural': 'Modüller',
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('domain', models.CharField(max_length=70)),
                ('logo', models.ImageField(upload_to='site')),
                ('logo_nav', models.ImageField(upload_to='site')),
                ('icon', models.ImageField(upload_to='site')),
                ('keywords', models.CharField(max_length=150)),
                ('post_detail', models.SmallIntegerField(default=1000, help_text='Haber detayında sayfa başına düşen karakter sayısı örn:1000', verbose_name='Haber Detay Karakter')),
                ('page_size', models.SmallIntegerField(default=5, help_text='Sayfa başına düşen haber sayısı', verbose_name='Haber Sayısı')),
                ('facebook', models.CharField(default='0', max_length=100)),
                ('twitter', models.CharField(default='0', max_length=100)),
                ('instagram', models.CharField(default='0', max_length=100)),
                ('linkedin', models.CharField(default='0', max_length=100)),
                ('pinterest', models.CharField(default='0', max_length=100)),
                ('youtube', models.CharField(default='0', max_length=100)),
                ('google_plus', models.CharField(default='0', max_length=100)),
                ('tumblr', models.CharField(default='0', max_length=100)),
                ('footer_text', models.CharField(max_length=250)),
                ('top_banner', models.ImageField(blank=True, null=True, upload_to='site')),
                ('iyzi_api', models.CharField(blank=True, help_text='İyzico api key', max_length=250, verbose_name='İyzi api key')),
                ('iyzi_secret_key', models.CharField(blank=True, help_text='İyzico secret key', max_length=250, verbose_name='İyzico secret key')),
                ('gmap', models.TextField(verbose_name='Google Map Link')),
                ('gapi_key', models.CharField(max_length=100)),
                ('view_id', models.CharField(max_length=100)),
                ('jsonFile', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/home/murat/Desktop/ecommerce', location='/home/murat/Desktop/ecommerce'), upload_to='newsadmin/analitik/')),
            ],
            options={
                'verbose_name': 'Site Ayar',
                'verbose_name_plural': 'Site Ayarları',
            },
        ),
    ]
