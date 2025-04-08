# filters.py
import django_filters
from .models import Patching

class PatchingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Patching
        fields = ['machine']  # add more fields as needed
