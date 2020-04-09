from django.db import models


class NewClient(models.Model):
    STATUS = [
        ('OK', 'Договор заключен'),
        ('Think', 'Думает'),
        ('Decline', 'Отказ'),
        ('Passport', 'Ожидаем данные паспорта'),
        ('Another', 'Другое'),
    ]

    FROM = [
        ('Site', 'С сайта'),
        ('Agent', 'Агент'),
        ('Office', 'В офисе'),
        ('Phone','По телефону')
    ]

    city = models.CharField("Город",max_length=100)
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Номер телефона", max_length=100)
    message = models.CharField("Сообщение", max_length=100, blank=True)
    is_send = models.BooleanField("Отправлено в телеграм",null=True, default=None, )
    manager = models.CharField("Менеджер", max_length=100,null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS,null=True, blank=True)
    message_id = models.IntegerField("message id", null=True,default=None, blank=True)
    reply_id = models.IntegerField("reply_id", null=True,default=None, blank=True)
    comment = models.TextField("Комментарий", max_length=255,null=True, blank=True)
    ticket_from =  models.CharField("Заявка",max_length=10, choices=FROM,null=True, blank=True)
    district = models.CharField("Район",max_length=100,null=True, blank=True)