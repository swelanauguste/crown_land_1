# Generated by Django 3.2.8 on 2021-11-06 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_alter_property_year_occupied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
