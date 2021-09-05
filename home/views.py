from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context