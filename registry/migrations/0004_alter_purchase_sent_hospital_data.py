# Generated by Django 4.registry.7 on 2023-04-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0003_alter_purchase_hospital_name_delete_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='sent_hospital_data',
            field=models.DateField(blank=True, null=True, verbose_name='Дата отправки в больницу'),
        ),
    ]