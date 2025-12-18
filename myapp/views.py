from django.shortcuts import render
from django.contrib import messages
from myapp.forms import MessageForm
import os
from django.http import FileResponse, Http404
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            instance = form.save()

            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            msg_text = form.cleaned_data['message']

            # Safe email sending (won't crash app)
            try:
                send_mail(
                    subject=f"New message from {name}",
                    message=f"From: {sender_email}\n\nMessage:\n{msg_text}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=True,   # IMPORTANT
                )
            except Exception as e:
                print("Email error:", e)

            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'There was an error in your form. Please correct it and try again.')
    else:
        form = MessageForm()

    return render(request, 'index.html', {'form': form})


def download_resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'resume.pdf')

    if os.path.exists(file_path):
        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename='resume.pdf'
        )
    else:
        raise Http404("Resume not found")
