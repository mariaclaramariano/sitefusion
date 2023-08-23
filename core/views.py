from django.http import HttpResponse
from django.views.generic import FormView
from .forms import ContatoForms
from django.urls import reverse_lazy
from .models import Servico, Equipe, features
from  django.contrib import messages

class indexview(FormView):
    template_name = 'index.html'
    form_class= ContatoForms
    sucess_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super(indexview, self).get_context_data(**kwargs)
        context ['Servicos']= Servico.objects.all()
        context['equipes'] = Equipe.objects.all()
        context['features']= features.objects.all()
        return context
    
    def form_valid(self, form, *args, **kwargs ):
        form.send_email()
        messages.success(self.request, 'email enviado com sucesso')
        return super(indexview, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'erro ao enviar!')
        return super(indexview, self).form_invalid(form, *args, **kwargs)
        
        