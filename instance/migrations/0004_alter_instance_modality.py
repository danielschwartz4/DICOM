# Generated by Django 3.2.16 on 2022-12-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0003_instance_modality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='modality',
            field=models.CharField(choices=[('MRI', 'Mri'), ('CT', 'Ct'), ('US', 'Us'), ('NA', 'Na')], default='NA', max_length=3),
        ),
    ]