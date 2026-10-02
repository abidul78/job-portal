from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from jobs.models import Application

from .forms import CustomUserCreationForm, ProfileForm, ResumeUploadForm
from .models import CustomUser


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('job-list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def upload_resume(request):
    if request.user.role != 'seeker':
        messages.error(request, 'Only job seekers can upload resumes.')
        return redirect('job-list')

    if request.method == 'POST':
        form = ResumeUploadForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume uploaded successfully!')
            return redirect('upload-resume')
    else:
        form = ResumeUploadForm(instance=request.user)

    return render(request, 'upload_resume.html', {'form': form})


@login_required
def edit_profile(request):
    if request.user.role != 'seeker':
        messages.error(request, 'Only job seekers have applicant profiles.')
        return redirect('job-list')

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('edit-profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def applicant_profile(request, user_id):
    if request.user.role != 'employer':
        messages.error(request, 'Only employers can view applicant profiles.')
        return redirect('job-list')

    applicant = get_object_or_404(CustomUser, id=user_id, role='seeker')

    has_application = Application.objects.filter(
        applicant=applicant,
        job__posted_by=request.user,
    ).exists()

    if not has_application:
        messages.error(request, 'You can only view applicants to your own jobs.')
        return redirect('employer-dashboard')

    return render(
        request,
        'applicant_profile.html',
        {'applicant': applicant},
    )
