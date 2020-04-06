from django.db import models

class NewClient(models.Model):
    STATUS = [
        ('OK', 'Договор заключен'),
        ('Think', 'Думает'),
        ('Decline', 'Отказ'),
        ('Another', 'Другое'),
    ]

    city = models.CharField("Город",max_length=100)
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Номер телефона", max_length=100)
    message = models.CharField("Сообщение", max_length=100)
    is_send = models.BooleanField("Отправлено в телеграм", default=None)
    manager = models.CharField("Менеджер", max_length=100)
    status = models.CharField(max_length=10, choices=STATUS)