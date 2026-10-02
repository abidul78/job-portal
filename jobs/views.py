from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Job, Application
from .forms import JobForm


# -------------------------
# JOB LIST
# -------------------------

class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'all_jobs'
    paginate_by = 6

    def get_queryset(self):
        queryset = Job.objects.all().order_by('-date_posted')

        query = self.request.GET.get('q')
        location = self.request.GET.get('location')
        company = self.request.GET.get('company')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

        if location:
            queryset = queryset.filter(
                location__icontains=location
            )

        if company:
            queryset = queryset.filter(
                company_name__icontains=company
            )

        return queryset


# -------------------------
# JOB DETAIL
# -------------------------

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['already_applied'] = Application.objects.filter(
                job=self.object,
                applicant=self.request.user
            ).exists()
        else:
            context['already_applied'] = False

        return context


# -------------------------
# CREATE JOB
# -------------------------

class JobCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView
):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'
    success_url = reverse_lazy('job-list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.role == 'employer'


# -------------------------
# EDIT JOB
# -------------------------

class JobUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'
    success_url = reverse_lazy('employer-dashboard')

    def test_func(self):
        job = self.get_object()

        return (
            self.request.user.role == 'employer'
            and job.posted_by == self.request.user
        )


# -------------------------
# DELETE JOB
# -------------------------

class JobDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('employer-dashboard')

    def test_func(self):
        job = self.get_object()

        return (
            self.request.user.role == 'employer'
            and job.posted_by == self.request.user
        )


# -------------------------
# MY APPLICATIONS
# -------------------------

class MyApplicationListView(
    LoginRequiredMixin,
    ListView
):
    model = Application
    template_name = 'my_applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        ).select_related(
            'job'
        ).order_by(
            '-date_applied'
        )


# -------------------------
# EMPLOYER DASHBOARD
# -------------------------

class EmployerDashboardView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    ListView
):
    model = Job
    template_name = 'employer_dashboard.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.filter(
            posted_by=self.request.user
        ).prefetch_related(
            'application_set__applicant'
        ).order_by(
            '-date_posted'
        )

    def test_func(self):
        return self.request.user.role == 'employer'


# -------------------------
# APPLY FOR JOB
# -------------------------

@login_required
@require_POST
def apply_job(request, pk):
    job = get_object_or_404(
        Job,
        pk=pk
    )

    if request.user.role != 'seeker':

        messages.error(
            request,
            'Only job seekers can apply for jobs.'
        )

        return redirect(
            'job-detail',
            pk=pk
        )

    application, created = Application.objects.get_or_create(
        job=job,
        applicant=request.user
    )

    if created:

        messages.success(
            request,
            'Application submitted successfully.'
        )

    else:

        messages.info(
            request,
            'You have already applied for this job.'
        )

    return redirect(
        'job-detail',
        pk=pk
    )


# -------------------------
# UPDATE APPLICATION STATUS
# -------------------------

@login_required
@require_POST
def update_application_status(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk
    )

    if request.user.role != 'employer':

        messages.error(
            request,
            'Only employers can update application status.'
        )

        return redirect('job-list')

    if application.job.posted_by != request.user:

        messages.error(
            request,
            'You cannot manage applications for this job.'
        )

        return redirect(
            'employer-dashboard'
        )

    new_status = request.POST.get('status')

    valid_statuses = {choice[0] for choice in Application.STATUS_CHOICES}

    if new_status not in valid_statuses:

        messages.error(
            request,
            'Invalid application status.'
        )

        return redirect(
            'employer-dashboard'
        )

    application.status = new_status
    application.save()

    messages.success(
        request,
        'Application status updated successfully.'
    )

    return redirect(
        'employer-dashboard'
    )