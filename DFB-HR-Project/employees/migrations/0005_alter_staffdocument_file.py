# Generated by Django 3.2.4 on 2021-07-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_donors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdocument',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]
