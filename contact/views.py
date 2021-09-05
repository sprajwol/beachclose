from django.views.generic import TemplateView

# Create your views here.
class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['contact_page'] = 'current-menu-item'

        return context