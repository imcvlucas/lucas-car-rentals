# Generated by Django 4.0.6 on 2022-08-15 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0002_category_product_alter_rent_vehicle_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='id',
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
