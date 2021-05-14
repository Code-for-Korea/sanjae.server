from django.db import models

# TODO 앱 이름과 모델 이름을 구분하는 게 좋지 않을까..
class Case(models.Model):
    case_number = models.CharField(max_length=255) # 보통 13자 이내
    court_name = models.CharField(max_length=255) # 보통 11자 이내
    ruling_type = models.CharField(max_length=255, blank=True) # 보통 4자 이내
    case_type = models.CharField(max_length=255, blank=True) # 보통 7자 이내
    issue_category = models.CharField(max_length=255, blank=True) # 보통 7자 이내
    ruling_text = models.TextField()
    case_title = models.CharField(max_length=255) # 보통 42자 이내
    related_case = models.CharField(max_length=255, blank=True) # 보통 142자 이내
    # 연관사건이 ForeignKey가 될 수 있을까? 현재 목록에 없는 사건번호도 있어서 일괄적용은 어려울 듯.
    # 하지만 db에 존재하는 사건일 경우 조회할 수 있으면 좋겠다
    working_condition = models.CharField(max_length=255, blank=True, default='')
    disease_type = models.CharField(max_length=255, blank=True, default='')

    # TODO 사건연도 분리
    # TODO 법원 이름 띄어쓰기 다른 케이스 존재. 통일
    # TODO 법원이 별도 테이블로 존재해야 하는가?

    def __str__(self):
        return self.case_number