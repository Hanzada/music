# Generated by Django 2.1.2 on 2018-10-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0007_auto_20181003_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
