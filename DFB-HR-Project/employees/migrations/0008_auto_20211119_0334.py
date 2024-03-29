# Generated by Django 3.2.4 on 2021-11-19 02:34

from django.db import migrations, models
import employees.custom_storage


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_staffdocument_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='default.png', storage=employees.custom_storage.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='staffdocument',
            name='file',
            field=models.FileField(storage=employees.custom_storage.MediaStorage(), upload_to=''),
        ),
    ]
