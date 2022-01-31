# Generated by Django 4.0 on 2022-01-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_productCaption', models.CharField(max_length=50)),
                ('m_productImage', models.ImageField(upload_to='img/%y')),
                ('m_productPrice', models.FloatField(null=True)),
                ('m_productQuantity', models.IntegerField(null=True)),
            ],
        ),
    ]