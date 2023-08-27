from django.shortcuts import redirect
from django.urls import reverse


def wagtail_admin_login(request):
    allauth_login_url = reverse('account_login')
    next_param = request.GET.get('next')
    if next_param:
        allauth_login_url += f'?next={next_param}'

    return redirect(allauth_login_url)
