# Generated by Django 4.registry.7 on 2023-03-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_purchase_pdf_scan_alter_purchase_comment_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='hospital_name',
            field=models.CharField(max_length=150, verbose_name='Название больницы'),
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]
