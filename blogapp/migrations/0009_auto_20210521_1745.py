# Generated by Django 3.2.3 on 2021-05-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20210521_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sno',
        ),
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
