# Generated by Django 4.2 on 2024-10-20 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='Название локации')),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20, verbose_name='Широта локации')),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20, verbose_name='Долгота локации')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
                'ordering': ('name',),
            },
        ),
        migrations.AddIndex(
            model_name='locations',
            index=models.Index(fields=['name'], name='weather_loc_name_2a97bb_idx'),
        ),
    ]
