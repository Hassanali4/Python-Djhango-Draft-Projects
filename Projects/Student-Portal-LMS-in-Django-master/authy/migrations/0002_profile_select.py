# Generated by Django 3.2.3 on 2021-06-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='select',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium')], default='Base', max_length=8, verbose_name='Package'),
        ),
    ]