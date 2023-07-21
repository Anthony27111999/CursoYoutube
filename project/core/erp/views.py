from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CategoryCreateForm
from .models import Category
from django.utils.decorators import method_decorator


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    # Este decorator no deja acceder a la persona que no este logueada
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as ex:
            data['error'] = str(ex)

        return JsonResponse(data)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of category'
        return context


def category_list(request):
    data = {
        'title': 'List of category',
        'categoria': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category:category_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as ex:
            data['error'] = str(ex)

        return JsonResponse(data)

        # print(request.POST)
        # form = CategoryCreateForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect(self.success_url)
        # self.object = None
        # context = self.get_context_data(**kwargs)
        # context['form'] = form
        # context['create_url'] = reverse_lazy('category:category_list')
        # return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add category'
        context['entity'] = 'Category'
        context['list_url'] = reverse_lazy('category:category_list')
        context['action'] = 'add'
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update category'
        context['entity'] = 'Category'
        context['list_url'] = reverse_lazy('category:category_list')
        context['action'] = 'edit'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete category'
        context['entity'] = 'Category'
        context['list_url'] = reverse_lazy('category:category_list')
        return context
