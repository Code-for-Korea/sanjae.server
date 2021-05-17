from django.db import migrations, models
from django.conf import settings
import csv
import opendata_sanjae

def initialize_data(apps, schema_editor):
    Ruling = apps.get_model('case_app', 'Ruling')
    db_alias = schema_editor.connection.alias

    api = opendata_sanjae.API()
    api.ENCODED_SERVICE_KEY = settings.OPENDATA_API_KEY

    all_cases = api.get_all_cases()
    ruling_list = [
        Ruling(
            case_number=case[0],
            court_name=case[1],
            ruling_type=case[2],
            case_type=case[3],
            issue_category=case[4],
            ruling_text=case[5],
            case_title=case[6],
            related_case=case[7],
        ) for case in all_cases
    ]

    # ruling_list = []
    # with open('data/cases_2021_5_14.csv', encoding='utf8') as csvfile:
    #     reader = csv.reader(csvfile)
    #     rows = [row for row in reader] # TODO 두 번에 나눠서 처리하지 말고 한 번에 헤더 건너뛰고 일겅
    #     for row in rows[1:]:
    #         ruling_list.append(
    #             Ruling(
    #                 case_number=row[0],
    #                 court_name=row[1],
    #                 ruling_type=row[2],
    #                 case_type=row[3],
    #                 issue_category=row[4],
    #                 ruling_text=row[5],
    #                 case_title=row[6],
    #                 related_case=row[7],
    #             )
    #         )
    Ruling.objects.using(db_alias).bulk_create(ruling_list)

class Migration(migrations.Migration):
    dependencies = [
         ('case_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initialize_data),
    ]

