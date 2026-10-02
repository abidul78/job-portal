from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import CustomAuthenticationForm
from .views import applicant_profile, edit_profile, signup_view, upload_resume


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            authentication_form=CustomAuthenticationForm,
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='job-list'),
        name='logout',
    ),
    path('upload-resume/', upload_resume, name='upload-resume'),
    path('profile/', edit_profile, name='edit-profile'),
    path(
        'applicant/<int:user_id>/',
        applicant_profile,
        name='applicant-profile',
    ),
]
