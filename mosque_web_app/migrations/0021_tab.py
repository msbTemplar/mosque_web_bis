# Generated by Django 5.1.4 on 2025-02-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque_web_app', '0020_bestvideos_best_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_slug', models.SlugField(help_text='Identificador único de la pestaña (ej: home, about, event)', unique=True)),
                ('tab_nombre', models.CharField(max_length=100)),
                ('tab_description', models.TextField()),
                ('tab_url', models.URLField(blank=True, null=True, verbose_name='tab URL')),
                ('tab_img_url', models.ImageField(blank=True, max_length=5500, null=True, upload_to='tab_img_url_images/')),
                ('tab_file', models.FileField(blank=True, max_length=5500, null=True, upload_to='tab_file_files/')),
                ('tab_date_page', models.DateField(blank=True, help_text='Fecha de BestVideos', null=True)),
                ('tab_time_page', models.TimeField(blank=True, help_text='Hora de BestVideos', null=True)),
                ('tab_day_page', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que se creó el tab.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Última vez que se actualizó el tab.')),
                ('is_active', models.BooleanField(default=True, help_text='Define si este tab está activo y visible.')),
            ],
        ),
    ]
