# Generated by Django 4.2 on 2023-09-15 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_stock_underlying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Border_FetchedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MostActiveStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_json', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MostSpreadStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_json', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VolumeGainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_json', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol_name', models.CharField(max_length=100)),
                ('prev_high', models.CharField(max_length=100)),
                ('today_low', models.CharField(max_length=100)),
                ('today_high', models.CharField(max_length=100)),
                ('change_value', models.CharField(max_length=100)),
                ('change_percent', models.CharField(max_length=100)),
                ('prev_close', models.CharField(max_length=100)),
                ('today_volume', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]