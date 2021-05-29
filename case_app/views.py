from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from .models import Ruling


def redirect_to_rulings(request):
    response = redirect("/rulings/")
    return response


# Create your views here.


def list(request):
    query_params = request.GET
    sort = query_params.get("sort", "-case_number")

    # do something
    rulings_count = Ruling.objects.count()
    rulings_all = Ruling.objects.order_by(sort)
    page_size = 100
    paginator = Paginator(rulings_all, page_size)

    page_num = query_params.get("page", "1")
    try:
        page_num = int(page_num)
    except:
        page_num = 1

    ruling_list = paginator.get_page(page_num)

    context = {
        "ruling_list": ruling_list,
        "count": rulings_count,
        "sort": sort,
    }
    return render(request, "case_app/list.html", context)


def detail(request, ruling_id):
    ruling = get_object_or_404(Ruling, pk=ruling_id)
    context = {"ruling": ruling}
    return render(request, "case_app/detail.html", context)


@login_required(login_url="/login/")
def edit(request, ruling_id):
    ruling = get_object_or_404(Ruling, pk=ruling_id)
    context = {"ruling": ruling}
    return render(request, "case_app/edit.html", context)


@login_required(login_url="/login/")
def submit(request, ruling_id):
    ruling = get_object_or_404(Ruling, pk=ruling_id)
    context = {"ruling": ruling}
    try:
        ruling.disease_code = request.POST["disease_code"]
        ruling.disease_name = request.POST["disease_name"]
        ruling.causality = request.POST["causality"]
        ruling.working_condition = request.POST["working_condition"]
        ruling.save()
        return HttpResponseRedirect(
            reverse("case_app:detail", args=(ruling.id, )))
    except:
        context["error_message"] = "저장에 실패했습니다."
        return render(request, "case_app/edit.html", context)
