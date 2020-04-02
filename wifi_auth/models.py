from django.db import models



class Router(models.Model):
    router_name = models.CharField('Имя роутера', max_length=50)
    ip_address = models.GenericIPAddressField('IP-адрес')
    admin_login = models.CharField('Логин для входа', max_length=50)
    admin_password = models.CharField('Пароль для входа', max_length=50)
    available = models.BooleanField("Доступен", default=False)

    def __str__(self):
        return self.router_name

    class Meta():
        verbose_name = 'Роутер'
        verbose_name_plural = 'Роутеры'

