# Generated by Django 4.0 on 2022-01-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping_cart', '0002_delete_uiimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UiImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='UiImage/')),
            ],
        ),
    ]
