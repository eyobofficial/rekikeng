from django.db import migrations


def create_default_company(apps, _):
    Company = apps.get_model('pages', 'Company')
    Company.objects.get_or_create(name='Rekik Engineering')


def delete_default_company(apps, _):
    Company = apps.get_model('pages', 'Company')
    try:
        Company.objects.get(name='Rekik Engineering').delete()
    except Company.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=create_default_company,
            reverse_code=delete_default_company
        )
    ]
