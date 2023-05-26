# Generated by Django 4.2.1 on 2023-05-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=20)),
                ('link', models.URLField()),
                ('reviews', models.IntegerField()),
                ('screen_diagonal', models.CharField(blank=True, max_length=10, null=True)),
                ('sim_card_count', models.CharField(blank=True, max_length=10, null=True)),
                ('built_in_memory', models.CharField(blank=True, max_length=10, null=True)),
                ('front_camera', models.CharField(blank=True, max_length=20, null=True)),
                ('main_camera', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(default='not complete', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('status', models.CharField(default='not complete', max_length=20)),
            ],
        ),
    ]