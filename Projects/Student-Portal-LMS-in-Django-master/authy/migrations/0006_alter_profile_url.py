# Generated by Django 3.2.3 on 2021-06-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0005_auto_20210611_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.CharField(blank=True, default='abs', max_length=80, null=True),
        ),
    ]