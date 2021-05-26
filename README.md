# 산재보험 판례 판결문 목록

http://sanjae.codefor.kr/rulings/

연구자, 근로자, 일반 시민이 산업재해 판례 정보를 손쉽게 조회하고 상황에 따라 메타데이터를 추가할 수 있는 서비스입니다. 2021년 5월 현재 개발중입니다.

연관 프로젝트: https://github.com/Code-for-Korea/Industrial_disasters

## 프로젝트 구조

### 환경/의존성

- main 브랜치의 코드가 AWS Lightsail로 배포됩니다.
- Python 3, Django 3.2를 사용합니다.
- requirements.txt에 명시된 https://github.com/achimkoh/sanjae.crawler.git (opendata_sanjae 라이브러리)는 https://github.com/Code-for-Korea/Industrial_disasters 의 산재 판례 데이터 수집 코드를 파이썬 모듈 형태로 감싸놓은 것입니다.

### 프론트엔드 뷰

현재의 테스트용 프론트엔드 뷰는 django와 [bulma](https://bulma.io/)를 사용합니다.

`http://127.0.0.1:8000/rulings/`로 이동하면 장고 어드민을 이용하지 않고 DB에 등록된 판례 목록을 조회할 수 있습니다. 사건번호를 클릭하면 상세 내용을 조회할 수 있습니다. 회원으로 로그인할 경우 (staff/superuser일 필요 없음) 질병코드/질병명/업무환경 필드 편집이 가능합니다.

## 프로젝트에 기여하기

## [할 일 목록](https://github.com/Code-for-Korea/sanjae.server/projects/1)

1차 보완 개발 이슈들을 [issue](https://github.com/Code-for-Korea/sanjae.server/issues)에 적어두었습니다. 맡아서 해 보고 싶으신 일들 있으시면 아래쪽에 자기가 하겠다고 의견 남겨주시면 감사하겠습니다.

## 로컬에서 실행하는 방법

1. python 개발 환경을 구축합니다.
2. 프로젝트에 필요한 가상환경을 만듭니다.(권장사항)
3. `pip install -r requirements.txt --no-cache-dir` 로 django 및 필요 라이브러리를 설치합니다.
4. config/settings.py 하단의 OPENDATA_API_KEY 에 본인의 api 키를 설정합니다.
5. DB migrate를 합니다.(`python manage.py migrate`) (API에서 데이터 덤프를 받아 DB를 초기화하기 때문에 약 5~10분 소요)
6. admin 계정을 만듭니다.(`python manage.py createsuperuser`)
7. 개발용 서버를 실행합니다.(`python manage.py runserver`)
8. admin page에 로그인합니다. (`http://127.0.0.1:8000/admin`)
9. CASE BACKEND 하위의 Rulings를 클릭하면 항목 리스트를 볼 수 있으며, 리스트에서 사건번호를 클릭하면 해당 사건 세부 내용을 볼 수 있으며 편집도 할 수 있습니다.
