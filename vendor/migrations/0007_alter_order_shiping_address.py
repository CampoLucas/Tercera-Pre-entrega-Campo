# Generated by Django 4.1.7 on 2023-03-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_alter_order_shiping_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shiping_address',
            field=models.CharField(max_length=255),
        ),
    ]
