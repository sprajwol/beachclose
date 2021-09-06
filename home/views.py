from django.views.generic import TemplateView

from about.models import Testimonial
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.all()

        context['testimonials_data'] = testimonials
        context['home_page'] = 'current-menu-item'

        return context
