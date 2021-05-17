# sanjae.server

data/cases_2021_5_14.csv 파일 위치:

https://drive.google.com/file/d/1WVG04k1eaZccxxcdEjUS-tB5Qk1A0mBF/view?usp=sharing



# 로컬에서 실행하는 방법
1. python 개발 환경을 구축합니다.
2. 프로젝트에 필요한 가상환경을 만듭니다.(선택사항)
3. django를 설치합니다.
4. 프로젝트 Root(manage.py파일이 있는 폴더)에서 data라는 폴더를 만듭니다.
5. 초기화 할 데이터가 들어있는 엑셀 파일을 받아서(위의 구글문서 링크의 문서를 써도 됩니다.) data 폴더 안에 넣습니다.
6. 혹시 파일명이 다르다면, 위 이름으로 rename하거나, sanjae.server/case_app/migrations/0002_data_init.py 의 8행에 있는 파일명을 수정합니다.
7. DB migrate를 합니다.(python manage.py migrate)
8. admin 계정을 만듭니다.(python manage.py createsuperuser)
9. 개발용 서버를 실행합니다.(python manage.py runserver)
10. admin page에 로그인합니다. (http://127.0.0.1:8000/admin)
11. CASE BACKEND 하위의 Rulings를 클릭하면 항목 리스트를 볼 수 있으며, 리스트에서 사건번호를 클릭하면 해당 사건으 세부 내용을 볼 수 있으며 편집도 할 수 있습니다.