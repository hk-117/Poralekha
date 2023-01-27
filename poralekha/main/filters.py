import django_filters
from .models import Tutor,Tution


class TutorFilter(django_filters.FilterSet):

    class Meta:
        model=Tutor
        fields={
            'address_covered': ['icontains'],
            'preffered_medium': ['icontains'],
            'preffered_class': ['icontains'],
            'preffered_subject': ['icontains'],
            'expected_salary': ['gt','lt'],
            'gender': ['icontains'],
        }

class TutionFilter(django_filters.FilterSet):

    class Meta:
        model=Tution
        fields={
            'student_location': ['icontains'],
            'requirement_gender': ['icontains'],
            'student_subjects': ['icontains'],
            'salary': ['gt','lt'],
        }
