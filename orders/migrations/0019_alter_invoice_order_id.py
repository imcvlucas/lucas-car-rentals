# Generated by Django 4.0.6 on 2022-09-27 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_invoice_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='order_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
