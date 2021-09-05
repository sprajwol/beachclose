from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['about_page'] = 'current-menu-item'

        return context