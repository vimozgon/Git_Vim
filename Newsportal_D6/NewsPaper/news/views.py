from django.shortcuts import render, reverse, redirect
from .models import New, Category, CategoryToUser
from django.views.generic import ListView, DetailView, View, FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.core.paginator import Paginator
from .filters import NewFilter
from .forms import NewForm, UserForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import Form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from datetime import datetime
from django.dispatch import receiver
from django.core.mail import mail_managers
from django.db.models.signals import post_save, m2m_changed
from django.contrib.sites.shortcuts import get_current_site



class News(ListView):
    model = New
    context_object_name = 'news'
    template_name = 'news/posts.html'
    ordering = ['-dateCreation']
    author = 'authors'
    paginate_by = 10

    def get_filter(self):
        return NewFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }


class NewDetailView(DetailView):
    template_name = 'news/detail.html'
    queryset = New.objects.all()


class NewCreateView(CreateView):
    template_name = 'news/create.html'
    form_class = NewForm


class NewUpdateView(UpdateView):
    template_name = 'news/create.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)


class NewDeleteView(DeleteView):
    template_name = 'news/delete.html'
    queryset = New.objects.all()
    success_url = '/news/'


class MyView(PermissionRequiredMixin, View):
    permission_required = ('news.view_New')


class AddNew(PermissionRequiredMixin, CreateView):
    permission_required = ('news.view_New', 'news.add_New', 'news.change_New', 'news.delete_New')


class CategoryList(ListView):
    model = Category
    template_name = 'news/abonent_category.html'
    context_object_name = 'abonent_category'

    #def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['is_not_subscribers'] = Category.objects.filter(subscriber=subscriber, user=user)
    #     # context['is_subscribers'] = Category.objects.filter(subscriber=user, user=subscriber)
    #     context['user_subscribers'] = Category.objects.all()
    #     return context

    def post(self, request, *args, **kwargs):
        id_category = request.POST.getlist("Подписка")
        print(f'категория- {id_category} ')
        mass_cat = ''
        for id_cat in id_category:
            a = Category.objects.get(id=id_cat)
            a.subscribers.add(request.user)
            mass_cat = mass_cat + f'{a}; '

        send_mail(
            subject=f'{request.user.username} Вы подписаны на новости в категории {mass_cat}',
            message=f'{request.user.username} Вы подписаны на новости в категории {mass_cat}',
            from_email="skillfactorys@yandex.ru",
            recipient_list=[request.user.email],
        )
        return redirect('/news/')

