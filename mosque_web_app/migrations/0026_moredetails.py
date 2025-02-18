# Generated by Django 5.1.4 on 2025-02-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque_web_app', '0025_joinnow'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_details_slug', models.SlugField(help_text='Identificador único de la sección (ej: home, about, event)', unique=True)),
                ('more_details_nombre', models.CharField(max_length=100)),
                ('more_details_description', models.TextField()),
                ('more_details_url', models.URLField(blank=True, null=True, verbose_name='More Details URL')),
                ('more_details_img_url', models.ImageField(blank=True, max_length=5500, null=True, upload_to='more_details_img_url_images/')),
                ('more_details_file', models.FileField(blank=True, max_length=5500, null=True, upload_to='more_details_file_files/')),
                ('more_details_date_page', models.DateField(blank=True, help_text='Fecha de More Details', null=True)),
                ('more_details_time_page', models.TimeField(blank=True, help_text='Hora de More Details', null=True)),
                ('more_details_day_page', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que se creó el More Details.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Última vez que se actualizó el More Details.')),
                ('is_active', models.BooleanField(default=True, help_text='Define si este More Details está activo y visible.')),
            ],
        ),
    ]
