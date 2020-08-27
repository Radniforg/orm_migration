from django.views.generic import ListView
from django.shortcuts import render

from .models import Student

class StudentsListView(ListView):

    model = Student
    template = 'school/students_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





# def students_list(request):
#     template = 'school/students_list.html'
#     context = {}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = 'group'
#
#     return render(request, template, context)
