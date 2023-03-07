import django_filters

from .models import Property
 
 #filter properties by passing ?field_name=filter_value
 
class PropertyFilter(django_filters.FilterSet):
    advert_type = django_filters.CharFilter(
        field_name="advert_type", lookup_expr="iexact"
    )
    property_type = django_filters.CharFilter(
        field_name="property_type", lookup_expr="iexact"
    )
    city = django_filters.CharFilter(
        field_name="city", lookup_expr="iexact"
    )
    start_date = django_filters.DateFilter(field_name="built_date", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="built_date", lookup_expr="lte")
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Property
        fields = ["advert_type", "property_type", "price", "city", "built_date"]
