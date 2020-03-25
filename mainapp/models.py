from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Puples(models.Model):
    name = models.TextField("Имя", null=True)
    surname = models.TextField("Фамилия", null=True)
    rate = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True ,upload_to="puples_photo", default="puples_photo/user-2.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ученики"
        verbose_name_plural = "Ученики"

class Events(models.Model):
    date = models.DateField("Дата посещения")
    name = models.CharField("Название мероприятия", max_length=200)
    organization = models.CharField("Название организации", max_length=300)
    events = models.ForeignKey(Puples, verbose_name="Мероприятия", on_delete=models.SET_NULL, null=True)
    check = models.BooleanField(default=False)
    event_rate = models.PositiveIntegerField(default=1)
    verification_file = models.FileField(upload_to="verification_files/", null=True, verbose_name="Файл")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"

class Works(models.Model):
    date = models.DateField("Дата", null=True)
    theme = models.TextField("Название темы")
    name = models.TextField("Название работы")
    result = models.TextField(null=True, verbose_name="Результат")

    class Meta:
        verbose_name = "Работы учеников"
        verbose_name_plural = "Работы учеников"

class DaysTask(models.Model):
    date = models.DateField("Дата", null=True)
    name_task = models.CharField("Название задачи", max_length=200)
    discription_task = HTMLField("Описание задачи")
    result = models.CharField(null=True, verbose_name="Результат", max_length=200)
    count_answer = models.IntegerField(default=0, verbose_name="Количество человек, которые могут решить задачу (указать отрицательное число)")

    class Meta:
        verbose_name = "Задача дня"
        verbose_name_plural = "Задача дня"

