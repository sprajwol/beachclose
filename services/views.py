from django.views.generic import TemplateView

# Create your views here.
class ServicesView(TemplateView):
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['services_page'] = 'current-menu-item'

        return context