# Generated by Django 4.0.6 on 2022-09-27 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_alter_invoice_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.FloatField(),
        ),
    ]
