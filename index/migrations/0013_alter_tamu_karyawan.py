# Generated by Django 4.0.6 on 2022-08-28 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_alter_tamu_karyawan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamu',
            name='karyawan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.karyawan', verbose_name='karyawan_id'),
        ),
    ]
