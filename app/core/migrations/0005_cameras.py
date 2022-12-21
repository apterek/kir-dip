# Generated by Django 4.1.4 on 2022-12-21 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cabinets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id_cam', models.AutoField(primary_key=True, serialize=False)),
                ('cam_model', models.CharField(max_length=100)),
                ('addr', models.GenericIPAddressField()),
                ('in_pos', models.BooleanField()),
                ('cab_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cabinets')),
            ],
            options={
                'verbose_name': 'Cameras',
                'verbose_name_plural': 'Cameras',
            },
        ),
    ]