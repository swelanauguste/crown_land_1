# Generated by Django 3.2.8 on 2021-12-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='individualapplication',
            name='application_type',
        ),
        migrations.AddField(
            model_name='individualapplication',
            name='application_type',
            field=models.ManyToManyField(to='applications.ApplicationType'),
        ),
    ]