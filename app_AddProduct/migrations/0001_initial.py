# Generated by Django 4.0 on 2022-01-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productCaption', models.CharField(max_length=100)),
                ('productImage', models.ImageField(upload_to='img/%y')),
                ('productPrice', models.CharField(max_length=100)),
            ],
        ),
    ]
