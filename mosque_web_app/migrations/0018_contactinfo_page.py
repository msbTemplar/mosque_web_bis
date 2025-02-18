# Generated by Django 5.1.4 on 2025-01-19 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque_web_app', '0017_alter_donation_amount_collected_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='Facebook URL')),
                ('twitter_url', models.URLField(blank=True, null=True, verbose_name='Twitter URL')),
                ('linkedin_url', models.URLField(blank=True, null=True, verbose_name='LinkedIn URL')),
                ('instagram_url', models.URLField(blank=True, null=True, verbose_name='Instagram URL')),
                ('date_contact_info', models.DateField(blank=True, help_text='Fecha de footer', null=True)),
                ('time_contact_info', models.TimeField(blank=True, help_text='Hora de footer', null=True)),
                ('day_contact_info', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('img_url_contact_info', models.ImageField(blank=True, max_length=5500, null=True, upload_to='footer_images/')),
                ('file_contact_info', models.FileField(blank=True, max_length=5500, null=True, upload_to='footer_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que se creó el ContactInfo.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Última vez que se actualizó el ContactInfo.')),
                ('is_active', models.BooleanField(default=True, help_text='Define si este ContactInfo está activo y visible.')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Page Title')),
                ('url_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='URL Name')),
                ('is_dropdown', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Dropdown')),
                ('welcome_to_the_mosque', models.CharField(blank=True, help_text='Welcome to the mosque', max_length=500, null=True, verbose_name='Welcome to the mosque')),
                ('purity_comes_from_faith', models.TextField(blank=True, help_text='Purity comes from faith', null=True, verbose_name='Purity comes from faith')),
                ('date_page', models.DateField(blank=True, help_text='Fecha de footer', null=True)),
                ('time_page', models.TimeField(blank=True, help_text='Hora de footer', null=True)),
                ('day_page', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('img_url_page', models.ImageField(blank=True, max_length=5500, null=True, upload_to='footer_images/')),
                ('file_page', models.FileField(blank=True, max_length=5500, null=True, upload_to='footer_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que se creó el Home.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Última vez que se actualizó el Home.')),
                ('is_active', models.BooleanField(default=True, help_text='Define si este Home está activo y visible.')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subpages', to='mosque_web_app.page', verbose_name='Parent Page')),
            ],
        ),
    ]
