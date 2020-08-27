from django.urls import path
from school.views import StudentsListView
# from school.views import students_list

urlpatterns = [
    path('', StudentsListView.as_view(), name='students'),
]
