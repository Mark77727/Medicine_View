from django.db import models
from django.utils.html import format_html

"""Purchase and data"""


class Purchase(models.Model):
    hospital_name = models.CharField(
        max_length=150,
        verbose_name='Название больницы'


    )

    name = models.CharField(
        max_length=100,
        verbose_name='Объект закупки'


    )

    cost = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Цена'


    )

    arrive_data = models.DateField(
        verbose_name='Дата поступления'


    )

    sent_fin_data = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата отправки в ФУ'


    )

    sent_hospital_data = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата отправки в больницу'


    )

    sent_correct_data = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата отправки на доработку'


    )

    comment_text = models.TextField(
        null=True,
        blank=True,
        verbose_name='Комментарий'


    )

    p9 = models.BooleanField(
        verbose_name='Закупка по п.9'


    )

    repair = models.BooleanField(
        verbose_name='Ремонт'


    )

    develop_DED = models.BooleanField(
        verbose_name='ПСД'


    )

    PDF_scan = models.FileField(
        upload_to='PDF/',
        null=True,
        blank=True


    )
    def __str__(self):
        #return f'{self.hospital_name} {self.name} {self.cost} {self.p9}'
        return self.hospital_name

