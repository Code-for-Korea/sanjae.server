from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Ruling

# Create your views here.
def list(request):
    # do something
    rulings_count = Ruling.objects.count()
    rulings_all = Ruling.objects.order_by('-id')
    page_size = 10
    paginator = Paginator(rulings_all, page_size)

    query_params = request.GET
    page_num = query_params.get('page', '1')
    try:
        page_num = int(page_num)
    except:
        page_num = 1

    ruling_list = paginator.get_page(page_num)

    context = {
        'ruling_list': ruling_list,
        'count': rulings_count,
    }
    return render(request, 'case_app/list.html', context)


def detail(request, ruling_id):
    ruling = get_object_or_404(Ruling, pk=ruling_id)
    context = {'ruling': ruling}
    return render(request, 'case_app/detail.html', context)