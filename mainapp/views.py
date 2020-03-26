import os
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from .models import Puples, Events, Works, DaysTask
from .forms import EventsForm, AddEventForm, ImgChangeForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.urls import reverse_lazy
from django.core.mail import send_mail
import datetime


class MainView(ListView):
    puple = Puples
    queryset = Puples.objects.all()
    template_name = "main_page/main_page.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_new'] = Events.objects.filter(check=False).count()
        return context


class WrongTasksView(ListView):
    model = DaysTask
    template_name = "task_day_wrong.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['score'] = len([int(i) for i in DaysTask.objects.get().id_answers.split()])
        return context


class TasksView(ListView):
    model = DaysTask
    template_name = "task_day.html"
    mass_rate = [5, 3]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_task'] = DaysTask.objects.get().name_task
        context['discription_task'] = DaysTask.objects.get().discription_task
        context['date_task'] = DaysTask.objects.get().date
        context['count_of_answer'] = DaysTask.objects.get().count_answer
        context['count_of_puples'] = -DaysTask.objects.get().count_answer
        context['list_answ'] = [int(i) for i in DaysTask.objects.get().id_answers.split()]
        context['score'] = len([int(i) for i in DaysTask.objects.get().id_answers.split()])
        return context



    def post(self, request):
        if request.POST["result"] == DaysTask.objects.get().result and DaysTask.objects.get().count_answer < 0:
            Events.objects.create(name=f"Задача дня \"{DaysTask.objects.get().name_task}\"", date=datetime.date.today(),
                                  organization="ГБОУ Школа 1158",
                                  events=Puples.objects.get(user=request.user.id),
                                  event_rate=self.mass_rate[DaysTask.objects.get().count_answer], check=True,
                                  verification_file="123.jpg")
            task = DaysTask.objects.get()
            task.count_answer += 1
            task.id_answers += str(Puples.objects.get(user=request.user.id).user.id) + " "
            task.save()
            return redirect("/task_day")
        return redirect("/task_day/wrong")


def verificationFileDownload(request):
    usr_pk = request.POST.get("usr_pk")
    if not (request.user.is_superuser or str(request.user.pk) == usr_pk):
        return HttpResponseForbidden()
    file_base_dir = request.POST.get("file_base_dir")
    file_path = os.path.join(settings.MEDIA_ROOT, file_base_dir)
    try:
        with open(file_path, "rb") as file:
            response = HttpResponse(file.read(), content_type="application")
            response['Content-Disposition'] = 'inline; filename="verification' + os.path.splitext(file_base_dir)[
                1] + '"'
            return response
    except FileNotFoundError:
        return HttpResponseNotFound()


class PuplesView(ListView):
    puple = Puples
    template_name = "puples/puples_list.html"
    queryset = Puples.objects.order_by("-rate")

    def get_context_data(self, **kwargs):
        mass = [i[0] for i in Puples.objects.order_by("-rate").values_list('id')]
        for i in mass:
            pup = Puples.objects.get(id=i)
            pup.rate = sum(map(lambda x: x.event_rate, Events.objects.filter(events__pk=i, check=True)))
            pup.save()

        context = super().get_context_data(**kwargs)
        context['superusr'] = self.request.user.is_superuser
        context['pupil_pk'] = self.request.user.puples.pk
        context['events_new'] = Events.objects.filter(check=False).count()
        return context


def account(request):
    var = request.user.puples.pk
    return redirect("/statistic/pupil/" + str(var))


class ImgChangeView(DetailView):
    model = Puples
    pk_url_kwarg = "pk"
    template_name = "img_change.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_count'] = Events.objects.filter(events__pk=self.kwargs['pk'], check=True).count()
        context['events_new'] = Events.objects.filter(check=False).count()
        context['allevents'] = Events.objects.filter(events__pk=self.kwargs['pk']).order_by('-date')
        return context

    def get(self, request, pk):
        if request.user.is_superuser or request.user.puples.pk == pk:
            return super().get(request, pk)
        return HttpResponseForbidden()

    def post(self, request, pk):
        # raise IndexError
        puple = request.user.puples
        form = ImgChangeForm(request.POST, request.FILES, instance=puple)
        if form.is_valid():
            form.save()
            return redirect("/statistic/pupil/" + str(pk))
        return redirect(reverse_lazy("img_change", kwargs={'pk': pk}))


class PostDetailView(DetailView):
    model = Puples
    pk_url_kwarg = "pk"
    template_name = "puple_detail/puples_detail_end.html"

    def get(self, request, pk):
        if request.user.is_superuser or request.user.puples.pk == pk:
            return super().get(request, pk)
        return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_count'] = Events.objects.filter(events__pk=self.kwargs['pk'], check=True).count()
        context['events_new'] = Events.objects.filter(check=False).count()
        context['allevents'] = Events.objects.filter(events__pk=self.kwargs['pk']).order_by('-date')
        context['rate_event'] = sum(
            map(lambda x: x.event_rate, Events.objects.filter(events__pk=self.kwargs['pk'], check=True)))
        return context


class AddEventView(DetailView):
    model = Puples
    pk_url_kwarg = "pk"
    template_name = "add_event/add_event.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_count'] = Events.objects.filter(events__pk=self.kwargs['pk'], check=True).count()
        context['allevents'] = Events.objects.filter(events__pk=self.kwargs['pk']).order_by('-date')
        context['form'] = EventsForm()
        context['events_new'] = Events.objects.filter(check=False).count()
        context['rate_event'] = sum(
            map(lambda x: x.event_rate, Events.objects.filter(events__pk=self.kwargs['pk'], check=True)))
        return context

    def get(self, request, pk):
        if request.user.is_superuser or request.user.puples.pk == pk:
            return super().get(request, pk)
        return HttpResponseForbidden()

    def post(self, request, pk):
        form = EventsForm(request.POST, request.FILES)
        print(request.POST['date'], )
        if form.is_valid():
            send_mail("Добалено новое мероприятие",
                      f"Новое мероприятие от {Puples.objects.get(id=pk).surname} {Puples.objects.get(id=pk).name}\nДата посещения: {request.POST['date']}\nНазвание мероприятия:{request.POST['name']}",
                      "admin@it-class1158.site", ["ibkov@yandex.ru"])
            form = form.save(commit=False)
            form.events_id = pk
            form.save()
            return redirect("/statistic/pupil/" + str(pk))
        return redirect(reverse_lazy("add_event", kwargs={'pk': pk}))


class CheckList(ListView):
    model = Events
    queryset = Events.objects.filter(check=False)
    template_name = "CheckList/check_list.html"

    def get(self, request):
        if request.user.is_superuser:
            return super().get(request)
        else:
            return HttpResponseForbidden()

    def post(self, request):
        form = AddEventForm(request.POST)
        if form.is_valid():
            a = Events.objects.get(pk=request.POST["id"])
            f = AddEventForm(request.POST, instance=a)
            f.save()
        return redirect("/check_list/")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_new'] = Events.objects.filter(check=False).count()
        return context


class WorksView(ListView):
    queryset = Works.objects.all()
    template_name = "works/works.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_new'] = Events.objects.filter(check=False).count()
        return context


class IntensivView(ListView):
    queryset = Works.objects.all()
    template_name = "intensiv.html"


class ApplicantView(ListView):
    template_name = "applicant.html"
    queryset = Events.objects.all()
