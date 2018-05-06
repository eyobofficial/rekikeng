from django.views.generic import TemplateView
from . import models


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['company'] = models.Company.objects.all()[0]
        context['slide_list'] = models.Slide.objects.all()
        context['staff_list'] = models.Staff.objects.all()
        context['process_list'] = models.Process.objects.all()
        return context
