from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from news.models import User
from django.views.generic.edit import CreateView
from .models import BaseSignupForm


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseSignupForm
    success_url = '/'
