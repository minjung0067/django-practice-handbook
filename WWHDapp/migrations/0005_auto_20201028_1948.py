# Generated by Django 3.1.2 on 2020-10-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WWHDapp', '0004_auto_20201028_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='설명 입력'),
        ),
    ]
