from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F, Sum
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField("Имя", max_length=250)
    phonenumber = PhoneNumberField("Телефон",
                                   region="RU",
                                   db_index=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.name


class Salon(models.Model):
    name = models.CharField("Название", max_length=250)
    address = models.CharField("Адрес", max_length=250)

    class Meta:
        verbose_name = "Все салоны красоты"
        verbose_name_plural = "Все салоны красоты"

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField("Имя", max_length=250)
    photo = models.ImageField("Портрет",
                              upload_to="")

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    def __str__(self):
        return self.name


class Schedule(models.Model):
    date_time = models.DateTimeField("Дата и время",
                                     db_index=True)
    master = models.ForeignKey(Master,
                               verbose_name="Мастер",
                               related_name="shedules",
                               on_delete=models.CASCADE)
    client = models.ForeignKey(Client,
                               verbose_name="Клиент",
                               on_delete=models.CASCADE,
                               related_name="appointments")

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
        unique_together = ("master", "date_time")

    def __str__(self):
        return self.date_time


class Service(models.Model):
    name = models.CharField("Название", max_length=250)
    price = models.DecimalField("Цена",
                                max_digits=9,
                                decimal_places=2,
                                validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class SalonServiceItem(models.Model):
    salon = models.ForeignKey(Salon,
                              on_delete=models.CASCADE,
                              related_name="salons")
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                related_name="salons")
    master = models.ForeignKey(Master,
                               on_delete=models.CASCADE,
                               related_name="salons")

    class Meta:
        verbose_name = "Услуга салона красоты"
        verbose_name_plural = "Услуги салона красоты"

    def __str__(self):
        return f"{self.salon.name} - {self.service}"


class OrderQueryset(models.QuerySet):
    def fetch_total_price(self):
        order = self.annotate(
            price=Sum(F("items__salon_service__service__price"))
        )

        return order


class Order(models.Model):
    PAYMENT_STATUS = [
        ("Paid", "Оплачен"),
        ("Unpaid", "Не оплачен"),
    ]

    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name="orders")
    status = models.CharField("Статус оплаты",
                              max_length=10,
                              default="Unpaid",
                              db_index=True,
                              choices=PAYMENT_STATUS)
    promocode = models.CharField("Промокод через choice",
                                 max_length=250,
                                 blank=True,
                                 null=True)
    # purchase = добавить чеки оплаченных заказов + оплату
    objects = OrderQueryset.as_manager()

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"№{self.pk} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name="items")
    salon_service = models.ForeignKey(SalonServiceItem,
                                      on_delete=models.CASCADE,
                                      related_name="order_items")

    class Meta:
        verbose_name = "Позиция в заказе"
        verbose_name_plural = "Позиции в заказе"

    def __str__(self):
        return f"Услуга - {self.salon_service}"