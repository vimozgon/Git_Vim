from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers, send_mail
from news.models import New, CategoryToUser, Author, Category
from datetime import datetime
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site


@receiver(post_save, sender=New)
def notify_post_create(sender, instance, created, **kwargs):
    if created:
        print('свежие новости')
        print('***************Рассылка*******************')
        subject = f'{instance.title} {instance.newCategory} {instance.dateCreation.strftime("%d %m %Y")}'
        userlist = []
        link = ''.join(['http://', get_current_site(None).domain, ':8000/news'])
        message = f'Перейдите {link}/{instance.id}  чтобы прочесть статью.'
        for s in CategoryToUser.objects.all():
            mail = s.subscribers.email
            print(mail)
            userlist.append(mail)
            print(userlist)

            send_mail(
                subject=subject,
                message=message,
                from_email='skillfactorys@yandex.ru',
                recipient_list=[userlist],
            )
    else:
        print('Новостей нет')
    print('***************Рассылка*******************')

post_save.connect(notify_post_create, sender=New)
