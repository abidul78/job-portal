from django.urls import path

from .views import (
    EmployerDashboardView,
    JobCreateView,
    JobDeleteView,
    JobDetailView,
    JobListView,
    JobUpdateView,
    MyApplicationListView,
    apply_job,
    update_application_status,
)


urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('jobs/create/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('jobs/<int:pk>/apply/', apply_job, name='job-apply'),
    path('jobs/<int:pk>/edit/', JobUpdateView.as_view(), name='job-edit'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path(
        'my-applications/',
        MyApplicationListView.as_view(),
        name='my-applications',
    ),
    path(
        'employer-dashboard/',
        EmployerDashboardView.as_view(),
        name='employer-dashboard',
    ),
    path(
        'applications/<int:pk>/status/',
        update_application_status,
        name='application-status-update',
    ),
]
