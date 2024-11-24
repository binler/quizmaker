from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from framework.views import BaseCreateView, BaseDetailView, BaseListView

from .models import Question


class IndexView(LoginRequiredMixin, BaseListView):
    template_name = "quiz/index.html"
    context_object_name = "latest_question_list"
    title_bar = "Danh sách quiz"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-id")


class DetailView(LoginRequiredMixin, BaseDetailView):
    model = Question
    template_name = "quiz/detail.html"


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]


class CreateView(LoginRequiredMixin, BaseCreateView):
    model = Question
    template_name = "quiz/create.html"
    form_class = CreateQuizForm
    success_url = reverse_lazy("quiz:create")
    title_bar = "Quiz"

    def get_object(self, queryset=None):
        return None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        question_text = form.cleaned_data.get("question_text")
        question = form.save(commit=False)
        question.question_text = question_text
        question.save()
        return HttpResponse(status=200, headers={"HX-Redirect": reverse("quiz:list")})

    def form_invalid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)
