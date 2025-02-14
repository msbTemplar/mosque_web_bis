# Generated by Django 5.1.4 on 2025-02-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque_web_app', '0023_readmore'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnMore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learn_more_slug', models.SlugField(help_text='Identificador único de la pestaña (ej: home, about, event)', unique=True)),
                ('learn_more_nombre', models.CharField(max_length=100)),
                ('learn_more_description', models.TextField()),
                ('learn_more_url', models.URLField(blank=True, null=True, verbose_name='Learn More URL')),
                ('learn_more_img_url', models.ImageField(blank=True, max_length=5500, null=True, upload_to='learn_more_img_url_images/')),
                ('learn_more_file', models.FileField(blank=True, max_length=5500, null=True, upload_to='learn_more_file_files/')),
                ('learn_more_date_page', models.DateField(blank=True, help_text='Fecha de Learn More', null=True)),
                ('learn_more_time_page', models.TimeField(blank=True, help_text='Hora de Learn More', null=True)),
                ('learn_more_day_page', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que se creó el Learn More.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Última vez que se actualizó el Learn More.')),
                ('is_active', models.BooleanField(default=True, help_text='Define si este Learn More está activo y visible.')),
            ],
        ),
    ]
