# Generated by Django 5.1.4 on 2025-02-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosque_web_app', '0024_learnmore'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_now_slug', models.SlugField(help_text='Identificador único de la pestaña (ej: home, about, event)', unique=True)),
                ('join_now_nombre', models.CharField(max_length=100)),
                ('join_now_description', models.TextField()),
                ('join_now_url', models.URLField(blank=True, null=True, verbose_name='Join Now URL')),
                ('join_now_img_url', models.ImageField(blank=True, max_length=5500, null=True, upload_to='join_now_img_url_images/')),
                ('join_now_file', models.FileField(blank=True, max_length=5500, null=True, upload_to='join_now_file_files/')),
                ('join_now_date_page', models.DateField(blank=True, help_text='Fecha de Join Now', null=True)),
                ('join_now_time_page', models.TimeField(blank=True, help_text='Hora de Join Now', null=True)),
                ('join_now_day_page', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que se creó el Join Now.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Última vez que se actualizó el Join Now.')),
                ('is_active', models.BooleanField(default=True, help_text='Define si este Join Now está activo y visible.')),
            ],
        ),
    ]
