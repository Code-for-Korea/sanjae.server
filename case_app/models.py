from django.db import models
from django.conf import settings


class Ruling(models.Model):
    """
    산재보험 판례 판결문
    원자료 출처: https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15041878

    원 API에 존재하는 항목 [속성 이름: 항목설명 - 공공데이터포털 API의 해당항목 이름]
    case_number: 사건번호 - accNum
    court_name: 법원명 - courtName
    ruling_type: 사건결과 - kindA
    case_type: 사건유형 - kindB
    issue_category: 사고, 질병 구분 - kindC
    ruling_text: 산재판결문 내용 - nonContent
    case_title: 사건명 - Title

    그 밖의 항목
    related_case: 판결문에서 추출한 연관판결. f'{법원},{사건번호},{n심}-{법원},{사건번호},{n심}...' 형식의 문자열
    working_condition: 업무환경 (수기 입력)
    causality: 상당인과관계 (수기 입력)
    disease_code: 표준 질병코드 (KCD 8차 기준)
    disease_name: 질병명 (KCD 8차 기준)
    """

    case_number = models.CharField(max_length=255, help_text="사건번호")  # 보통 13자 이내
    court_name = models.CharField(max_length=255, help_text="법원")  # 보통 11자 이내
    ruling_type = models.CharField(
        max_length=255, blank=True, help_text="판결유형"
    )  # 보통 4자 이내
    case_type = models.CharField(
        max_length=255, blank=True, help_text="사건유형"
    )  # 보통 7자 이내
    issue_category = models.CharField(
        max_length=255, blank=True, help_text="사고질병구분"
    )  # 보통 7자 이내
    ruling_text = models.TextField(help_text="판결문")
    case_title = models.CharField(max_length=255, help_text="제목")  # 보통 42자 이내
    related_case = models.CharField(
        max_length=255, blank=True, help_text="연관사건"
    )  # 보통 142자 이내
    # 연관사건이 ForeignKey가 될 수 있을까? 현재 목록에 없는 사건번호도 있어서 일괄적용은 어려울 듯.
    # 하지만 db에 존재하는 사건일 경우 조회할 수 있으면 좋겠다
    working_condition = models.TextField(blank=True, help_text="업무환경")
    causality = models.TextField(blank=True, help_text="상당인과관계")
    disease_code = models.CharField(
        max_length=255, blank=True, default="", help_text="질병코드"
    )
    disease_name = models.CharField(
        max_length=255, blank=True, default="", help_text="질병코드"
    )

    last_modified = models.DateTimeField(auto_now=True, help_text="최근 수정 일시")
    last_modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="최근 수정한 사용자",
    )

    def __str__(self):
        return self.case_number
