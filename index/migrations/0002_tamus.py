# Generated by Django 4.0.6 on 2022-08-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tamus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('namaIntansi', models.CharField(max_length=100)),
                ('jaminan', models.CharField(max_length=100)),
                ('keperluan', models.CharField(max_length=100)),
                ('karyawan', models.CharField(max_length=100)),
                ('jumlahTamu', models.IntegerField()),
                ('foto', models.ImageField(upload_to='')),
                ('waktu', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tamus',
            },
        ),
    ]
