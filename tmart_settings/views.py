from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.edit import FormView
from .models import OurInformation , Contact
from .forms import ContactForm
# Create your views here.

class ContactView(FormView):
	template_name = 'settings/contact.html'
	form_class = ContactForm
	success_url = 'contact'

	def form_valid(self, form):
		subject = form.cleaned_data.get('subject')
		message = form.cleaned_data.get('message')
		try:
			qs = Contact.objects.get(user = self.request.user)
			qs.delete()
			Contact.objects.create(user = self.request.user , subject = subject , message = message)
		except:
			Contact.objects.create(user = self.request.user , subject = subject , message = message)

		messages.success(self.request , 'ممنون از پیام شما ! ما پاسخ را به ایمیلتان ارسال می کنیم')
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['object_list'] = OurInformation.objects.filter(active = True).first()
		return context