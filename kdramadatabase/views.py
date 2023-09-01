from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from sortable_listview import SortableListView

from .models import KDrama


# Create your views here.

class IndexView(SortableListView):
    allowed_sort_fields = {'name_eng': {'default_direction': '',
                                        'verbose_name': 'Title'},
                           'name_kor': {'default_direction': '',
                                        'verbose_name': 'Korean Title'},
                           'rating': {'default_direction': '',
                                        'verbose_name': 'Rating'},
                           'pub_date': {'default_direction': '-',
                                        'verbose_name': 'Published On'}}
    default_sort_field = 'pub_date'

    template_name = "kdramadatabase/index.html"
    context_object_name = "drama_list"
    model = KDrama

    # def get_queryset(self):
    #     return KDrama.objects.iterator()


class DetailView(generic.DetailView):
    template_name = "kdramadatabase/detail.html"
    context_object_name = "drama"

    def get_queryset(self):
        return KDrama.objects.filter(pub_date__lte=timezone.now())
