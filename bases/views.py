from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic


class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):

    login_url = "bases:login"
    raise_exception = False
    redirect_field_name = "redirect_to"


    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))



def home(request):
    #Importamos nuestro modelo
    from solicitudes.models import Solicitud

#  Aqui filtramos el total de becas
    becas = Solicitud.objects.count()

# Y Aqui por los filtramos por su estado de entrega
    b = Solicitud.objects.filter(entrega='ENTREGADO').count()
    n = Solicitud.objects.filter(entrega='NO ENTREGADO').count()


    return render(request, 'bases/home.html', {'becas': becas, 'b': b, 'n': n})


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name = "bases/sin_privilegios.html"
