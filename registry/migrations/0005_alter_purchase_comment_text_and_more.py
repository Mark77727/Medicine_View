# Generated by Django 4.registry.7 on 2023-04-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0004_alter_purchase_sent_hospital_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='comment_text',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='sent_correct_data',
            field=models.DateField(blank=True, null=True, verbose_name='Дата отправки на доработку'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='sent_fin_data',
            field=models.DateField(blank=True, null=True, verbose_name='Дата отправки в ФУ'),
        ),
    ]