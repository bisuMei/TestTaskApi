from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.conf import settings
from django.conf.urls.static import static


class MyHack(auth_views.PasswordResetView):
    success_url = reverse_lazy('training:password_reset_done')


urlpatterns = [
    path('', views.index, name="home"),
    path('employees/', views.all_employees, name='employees'),
    path('details/', views.employee_details, name='details'),

    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
