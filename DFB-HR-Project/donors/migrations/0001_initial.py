# Generated by Django 3.2.4 on 2021-07-12 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donor', to='employees.employee')),
            ],
        ),
    ]