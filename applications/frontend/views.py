from django.views.generic import TemplateView, ListView, DetailView


class FrontendView(TemplateView):
    def get_template_names(self):
        return self.kwargs['slug']
