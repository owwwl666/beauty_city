from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Registration(models.Model):
    firstname= models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    phonenumber = PhoneNumberField(verbose_name="Номер телефона",
                                   db_index=True)

    class Meta:
        verbose_name = "Зарегистрированный пользователь"
        verbose_name_plural = "Зарегистрированные пользователи"

    def __str__(self):
        return f"{self.firstname} {self.phonenumber}"
