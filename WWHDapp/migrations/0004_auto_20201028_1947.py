# Generated by Django 3.1.2 on 2020-10-28 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WWHDapp', '0003_category_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='WWHDapp.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='0'),
        ),
    ]
