# Generated by Django 2.1.2 on 2018-10-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0006_auto_20181003_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
