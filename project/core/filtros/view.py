from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView

from core.erp.models import Product
from core.filtros.form import TestForm


class TestView(TemplateView):
    template_name = 'test.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '------------------------------'}]
                for i in Product.objects.filter(cate_id=request.POST['id']):
                    print('paso')
                    data.append({'id': i.id, 'text': i.name})
                pass
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as ex:
            print(str(ex))

        # Convertir el diccionario a formato JSON y enviarlo como respuesta JSON
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select anidado | Django'
        context['form'] = TestForm()
        return context
