from django.urls import path
from . import views, filters
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.conf import settings
from django.conf.urls.static import static


class MyHack(auth_views.PasswordResetView):
    success_url = reverse_lazy('training:password_reset_done')


urlpatterns = [
    path('', views.index, name="home"),
    path('details/', views.employee_details, name='details'),
    path('employees/', views.EmployeeView.as_view()),
    path('employee/', filters.EmployeeList.as_view()),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', MyHack.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy('firm_api:password_reset_compete')
         ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name="register"),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


