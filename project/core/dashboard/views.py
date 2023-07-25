from django.shortcuts import render
from django.views.generic import TemplateView

class DashBoardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = "Panel de admin."
        return context
