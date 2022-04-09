# Generated by Django 4.0.3 on 2022-04-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('citizenship', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
