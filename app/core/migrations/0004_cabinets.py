# Generated by Django 4.1.4 on 2022-12-21 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_faces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinets',
            fields=[
                ('id_cab', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('floor', models.IntegerField()),
                ('dep_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.department')),
            ],
            options={
                'verbose_name': 'Cabinet',
                'verbose_name_plural': 'Cabinets',
            },
        ),
    ]