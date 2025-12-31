from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import ContactMessage

# Création des vues des applications 

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# def home_pages_views(request):
#     context = {
#        "nom": "Gédéon",
#         "age": 25,
#         "couleurs": ["Noir", "Blanc", "Bleu", "Jaune", "Orange", "Rouge"],
#         "est_connecte": False
#    }
#     return render(request, "home.html", context) 

def apropos_pages_views(request):
    return render(request, "apropos.html")

@login_required
def contact_pages_views(request):
    success_msg = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_msg = "Votre message a bien été envoyé !"
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        "form": form,
        "success_msg": success_msg
    }
    return render(request, "contact.html", context)

class MessageListView(LoginRequiredMixin, ListView):
    model = ContactMessage
    template_name = "message_list.html"
    context_object_name = "message_list"

    def get_queryset(self):
        return ContactMessage.objects.filter(is_treated = False)

# def message_list_views(request):
#     messages = ContactMessage.objects.all()
#     context = {
#        "message_list": messages
#     }
#     return render(request, "message_list.html", context)  


