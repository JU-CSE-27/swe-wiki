# Generated by Django 4.0 on 2022-01-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image', '0002_image_price_image_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_productCaption', models.CharField(max_length=50)),
                ('m_productImage', models.ImageField(upload_to='img/%y')),
                ('m_productPrice', models.FloatField(null=True)),
                ('m_productQuantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
