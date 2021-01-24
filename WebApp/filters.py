import django_filters
from django_filters import CharFilter
from .models import *


class UniversityFilter(django_filters.FilterSet):
    uni_city = CharFilter(field_name='uni_city', lookup_expr='icontains')
    uni_type = CharFilter(field_name='uni_type', lookup_expr='icontains')

    class Meta:
        model = UniversityDetail
        fields = ('uni_city', 'uni_type', 'uni_rank')

    def __init__(self, *args, **kwargs):
        super(UniversityFilter, self).__init__(*args, **kwargs)
        self.filters['uni_city'].label = "City"
        self.filters['uni_type'].label = "Type"
        self.filters['uni_rank'].label = "Rank"
