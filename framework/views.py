from django.http import HttpRequest
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
)
from django_htmx.middleware import HtmxDetails


class BaseTitleMixin:
    title_bar = ""

    def get_title_bar(self):
        return self.title_bar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_bar"] = self.get_title_bar()
        return context


class BaseTemplateView(BaseTitleMixin, TemplateView):
    pass


class BaseListView(BaseTitleMixin, ListView):
    pass


class BaseDetailView(BaseTitleMixin, DetailView):
    pass


class BaseCreateView(BaseTitleMixin, CreateView):
    pass


class BaseDeleteView(BaseTitleMixin, DeleteView):
    pass


# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails
