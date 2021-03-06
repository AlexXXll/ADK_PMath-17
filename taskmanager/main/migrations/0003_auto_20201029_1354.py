# Generated by Django 3.1.2 on 2020-10-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201025_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.FileField(blank=True, upload_to='image/blog/%Y/%m/%d', verbose_name='Ссылка картинки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
