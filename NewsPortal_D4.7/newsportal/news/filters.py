# импортируем filterset, чем-то напоминающий знакомые дженерики
from django_filters import FilterSet, DateTimeFromToRangeFilter
from django_filters.widgets import DateRangeWidget, RangeWidget
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    dateCreation = DateTimeFromToRangeFilter(lookup_expr=(
        'icontains'), widget=RangeWidget(attrs={'type': 'datetime-local'}))

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах

    class Meta:
        model = Post
        # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {'author', 'dateCreation', 'categoryType'}
