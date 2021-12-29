# Generated by Django 3.2.3 on 2021-12-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0021_alter_post_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='trending',
            field=models.CharField(choices=[('trending', 'Trending'), ('normal', 'Normal')], default='Normal', max_length=50),
        ),
    ]
