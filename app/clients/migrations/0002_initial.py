# Generated by Django 3.2.8 on 2021-12-13 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='title_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='title',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='title_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clientidentification',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='clientidentification_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clientidentification',
            name='identification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_identifications', to='clients.client'),
        ),
        migrations.AddField(
            model_name='clientidentification',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='clientidentification_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='client_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.district'),
        ),
        migrations.AddField(
            model_name='client',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.title'),
        ),
        migrations.AddField(
            model_name='client',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='client_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]