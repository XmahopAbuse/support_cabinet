from django.db import models

class District(models.Model):
    name = models.CharField("Район",max_length=100)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self):
        return self.name

class NewClient(models.Model):
    STATUS = [
        ('OK', 'Договор заключен'),
        ('Think', 'Думает'),
        ('Decline', 'Отказ'),
        ('NoPassport', 'Ожидаем данные паспорта'),
        ('Another', 'Другое'),
        ('Office','Придет в офис'),
        ('Preview','В предварительные заявки')
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
    district = models.ForeignKey(District,on_delete=models.CASCADE,blank=True,default=None,null=True,verbose_name="Район")
    created =  models.DateTimeField("Создана",auto_now_add=True,null=True, blank=True)

