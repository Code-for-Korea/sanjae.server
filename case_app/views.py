from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from .models import Ruling

try:
    # 판례 목록 필터로 사용할 값들의 목록을 서버 실행시 정의해둡니다.
    court_name_list = [value['court_name'] for value in Ruling.objects.values(
        'court_name').distinct().order_by('court_name')]
    ruling_type_list = [value['ruling_type'] for value in Ruling.objects.values(
        'ruling_type').distinct().order_by('ruling_type')]
    case_type_list = [value['case_type'] for value in Ruling.objects.values(
        'case_type').distinct().order_by('case_type')]
    issue_category_list = [value['issue_category'] for value in Ruling.objects.values(
        'issue_category').distinct().order_by('issue_category')]
except:
    # DB 테이블이 생성되지 않았거나 하는 등의 이유로 오류가 나면 None으로 처리
    court_name_list = None
    ruling_type_list = None
    case_type_list = None
    issue_category_list = None


def redirect_to_rulings(request):
    '''
    루트(/)로 접속할 때 판결문 목록으로 리다이렉트하기 위해 사용하는 함수형 뷰
    '''
    response = redirect("/rulings/")
    return response


def list(request):
    '''
    판결문 목록
    '''
    query_params = request.GET

    # 검색 키워드가 존재하는지 확인
    search_keyword = query_params.get("search")
    if search_keyword:
        queryset = Ruling.objects.filter(
            Q(case_number__icontains=search_keyword) |
            Q(ruling_text__icontains=search_keyword) |
            Q(case_title__icontains=search_keyword)
        )
    else:
        queryset = Ruling.objects.all()

    # 판결문 목록 정렬 기준을 판단
    result_count = queryset.count()
    sort = query_params.get("sort", "-case_number")
    result = queryset.order_by(sort)

    page_size = query_params.get("page_size", "100")
    paginator = Paginator(result, int(page_size))

    page_num = query_params.get("page", "1")
    try:
        page_num = int(page_num)
    except:
        page_num = 1

    ruling_list = paginator.get_page(page_num)

    context = {
        "ruling_list": ruling_list,
        "count": result_count,
        "sort": sort,
        "court_name_list": court_name_list,
        "ruling_type_list": ruling_type_list,
        "case_type_list": case_type_list,
        "issue_category_list": issue_category_list,
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
        ruling.last_modified_by = request.user
        ruling.save()
        return HttpResponseRedirect(
            reverse("case_app:detail", args=(ruling.id, )))
    except:
        context["error_message"] = "저장에 실패했습니다."
        return render(request, "case_app/edit.html", context)
