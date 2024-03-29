from django.db import models

class Status(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)

class Issue(models.Model):
    summary = models.CharField(max_length=50, verbose_name='Краткое описание')
    description = models.TextField(null=True, blank=True, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', on_delete=models.RESTRICT, related_name='issues', verbose_name='Статус')
    types = models.ManyToManyField('webapp.Type', related_name='issues', verbose_name='Типы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f'{self.id}. {self.summary}'