# Generated by Django 3.2.3 on 2021-05-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='sno',
            field=models.AutoField(default='5', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
