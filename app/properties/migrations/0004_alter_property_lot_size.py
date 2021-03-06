# Generated by Django 3.2.8 on 2021-12-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_alter_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, help_text='in sq. ft.', max_digits=5),
        ),
    ]
