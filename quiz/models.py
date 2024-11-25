from django.db import models


class Question(models.Model):
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    def get_created_at_vn(self):
        return self.created_at.strftime("%d/%m/%Y %H:%M:%S")

    def get_updated_at_vn(self):
        return self.updated_at.strftime("%d/%m/%Y %H:%M:%S")


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
