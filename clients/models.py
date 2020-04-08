from django.db import models

class NewClient(models.Model):
    STATUS = [
        ('OK', 'Договор заключен'),
        ('Think', 'Думает'),
        ('Decline', 'Отказ'),
        ('Passport', 'Ожидаем данные паспорта'),
        ('Another', 'Другое'),
    ]

    city = models.CharField("Город",max_length=100)
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Номер телефона", max_length=100)
    message = models.CharField("Сообщение", max_length=100, blank=True)
    is_send = models.BooleanField("Отправлено в телеграм", default=None, )
    manager = models.CharField("Менеджер", max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    message_id = models.IntegerField("message id", default=None, blank=True)