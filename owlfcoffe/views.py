from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('index.html')
    context = {
        'menu': [
            {'nombre': 'Inicio', 'url': '/'},
            {'nombre': 'Quienes Somos', 'url': '/quienes-somos'},
            {'nombre': 'Servicios', 'url': '/servicios'},
            {'nombre': 'Contacto', 'url': '/contacto'}],
    }
    return HttpResponse(template.render(context, request))
