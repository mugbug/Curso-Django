from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            import ipdb; ipdb.set_trace()
            # Processa dados no form.cleaned_data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['leandroc@inatel.br']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/servicedesk/thanks')
    else:
        form = ContactForm()

    return render_to_response('contact.html', {'form': form,}, \
                                                RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html', RequestContext(request))
