# sanjae.server

## 로컬에서 실행하는 방법
1. python 개발 환경을 구축합니다.
2. 프로젝트에 필요한 가상환경을 만듭니다.(선택사항)
3. pip install -r requirements.txt로 django 및 필요 라이브러리를 설치합니다.
4. config/settings.py 하단의 OPENDATA_API_KEY 에 본인의 api 키를 설정합니다.
5. DB migrate를 합니다.(python manage.py migrate) (API에서 데이터 덤프를 받아 DB를 초기화하기 때문에 약 5분 소요)
6. admin 계정을 만듭니다.(python manage.py createsuperuser)
7. 개발용 서버를 실행합니다.(python manage.py runserver)
8. admin page에 로그인합니다. (http://127.0.0.1:8000/admin)
9. CASE BACKEND 하위의 Rulings를 클릭하면 항목 리스트를 볼 수 있으며, 리스트에서 사건번호를 클릭하면 해당 사건으 세부 내용을 볼 수 있으며 편집도 할 수 있습니다.