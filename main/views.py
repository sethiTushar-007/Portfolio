from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import *
from django.conf import settings

# Create your views here.

def phone_format(n):
    return n[:5] + ' ' + n[5:]

def index(request):
    profile = Profile.objects.all().values()[0]
    context = profile
    context['birth_date'] = context['birth_date'].strftime('%B %d, %Y')
    context['phone'] = phone_format(context['phone'])

    job_titles = JobTitle.objects.filter(is_active = True).values()
    context['job_titles'] = job_titles

    skills = Skill.objects.filter(is_active = True).values()
    context['skills'] = skills

    social_icons = SocialIcon.objects.filter(is_active = True).values()
    context['social_icons'] = social_icons

    return render(request, 'index.html', context)

def send_email(request):
    if request.is_ajax and request.method == 'POST':
        try:
            subject = 'Portfolio - ' + request.POST['contactSubject']
            body = render_to_string('email.html',{'sender_name': request.POST['contactName'], 'sender_email': request.POST['contactEmail'], 'sender_message': request.POST['contactMessage']})
            from_email = settings.EMAIL_HOST_USER
            to_email = Profile.objects.all()[0].email
            send_mail(subject, body, from_email, [to_email], fail_silently=True)
            return JsonResponse({'success': 'OK'}, status=200)
        except:
            return JsonResponse(status=404)