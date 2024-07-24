from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Subdivisions(MPTTModel):
    title = models.CharField(verbose_name='название подразделения', max_length=64, unique=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительское подразделение')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', ]]
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Staff(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=64, unique=False)
    position = models.CharField(verbose_name='должность', max_length=64)
    employment_date = models.DateTimeField(default=timezone.now, verbose_name='Дата приёма на работу')
    salary = models.DecimalField(verbose_name='Размер заработной платы', max_digits=128, decimal_places=2, default=0)
    subdivision = TreeForeignKey('Subdivisions', on_delete=models.PROTECT, verbose_name='Подразделение',
                                 related_name='staffs', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
