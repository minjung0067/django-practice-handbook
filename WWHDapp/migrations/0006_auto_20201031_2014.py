# Generated by Django 3.1.2 on 2020-10-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WWHDapp', '0005_auto_20201028_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
