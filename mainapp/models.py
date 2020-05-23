from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Puples(models.Model):
    STATUS_CHOICES = (
        ('ST10', 'Ученик 10 ИТ-класса'),
        ('ST11', 'Ученик 11 ИТ-класса'),
        ('APP', 'Кандидат в ИТ-класс'),
    )
    name = models.CharField("Имя", null=True, max_length=50)
    surname = models.CharField("Фамилия", null=True, max_length=100)
    rate = models.PositiveIntegerField("Рейтинг ученика", default=0)
    image = models.ImageField("Фотография профиля", blank=True, upload_to="puples_photo",
                              default="puples_photo/user-2.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default='', verbose_name="Связь с таблицей пользователей")
    status = models.CharField("Статуc", choices=STATUS_CHOICES, default='ST10', max_length=30)
    applicant_first_result = models.FloatField(blank=True, default=0)

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
    theme = models.CharField("Название темы", max_length=200, default="")
    name = models.CharField("Название работы", max_length=200, default="")
    result = models.CharField(null=True, verbose_name="Результат", max_length=300, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Работы учеников"
        verbose_name_plural = "Работы учеников"


class DaysTask(models.Model):
    date = models.DateField("Дата", null=True)
    name_task = models.CharField("Название задачи", max_length=200)
    discription_task = HTMLField("Описание задачи")
    result = models.CharField(null=True, verbose_name="Результат", max_length=200)
    count_answer = models.IntegerField(default=0,
                                       verbose_name="Количество человек, которые могут решить задачу (указать отрицательное число)")
    id_answers = models.CharField(default="", verbose_name="ID учеников, кто дал правильный ответ", max_length=200,
                                  blank=True)

    def __str__(self):
        return f"Задача: \"{self.name_task}\""

    class Meta:
        verbose_name = "Задача дня"
        verbose_name_plural = "Задача дня"
