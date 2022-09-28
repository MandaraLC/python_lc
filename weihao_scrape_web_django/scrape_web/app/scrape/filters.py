from datetime import timedelta

import django_filters

from .models import ScrapeResult


class ResultFilters(django_filters.FilterSet):
    """
    日期过滤
    """
    early_etd = django_filters.DateTimeFilter(field_name='etd', lookup_expr='gte', help_text='最早预计开航时间')
    late_etd = django_filters.DateTimeFilter(field_name='etd', method='get_last_time', help_text='最晚预计开航时间')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', help_text='最小金额')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', help_text='最大金额')

    def get_last_time(self, queryset, field_name, value):
        last_time = value + timedelta(days=1)
        return queryset.filter(etd__lte=last_time)

    class Meta:
        model = ScrapeResult
        fields = ['shipping_company', 'port_city', 'final_city', 'container_type', 'early_etd', 'late_etd',
                  'min_price', 'max_price']