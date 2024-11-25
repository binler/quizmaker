from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from framework.views import (BaseCreateView, BaseDeleteView, BaseDetailView,
                             BaseListView)

from .models import Question


class IndexView(LoginRequiredMixin, BaseListView):
    template_name = "quiz/list.html"
    context_object_name = "questions"
    title_bar = "Danh sách quiz"
    paginate_by = 10

    def get_queryset(self):
        """Return questions ordered by id."""
        return Question.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["is_paginated"]:
            # Get the page number from the query parameters, default to 1
            page = self.request.GET.get("page", 1)
            paginator = context["paginator"]
            try:
                questions = paginator.page(page)
            except PageNotAnInteger:
                questions = paginator.page(1)
            except EmptyPage:
                questions = paginator.page(paginator.num_pages)
            context["questions"] = questions
        return context


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


class DeleteView(LoginRequiredMixin, BaseDeleteView):
    # TODO: view confirm modal
    model = Question
    success_url = reverse_lazy("quiz:list")
    template_name = "quiz/confirm_delete.html"
    title_bar = "Xóa quiz"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponse(status=200, headers={"HX-Redirect": success_url})
