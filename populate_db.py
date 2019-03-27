import requests

import django
import os

app_key = 'appOMCxUoUICzw4U0'

headers = {
    'Authorization': 'Bearer keyBLrxoClNCGfF5f',
}

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vcfirms.settings")
django.setup()

from firms.models import Firm, Employee, Job


def update_attrs(model, data):

    print(f"updating {model.__class__.__name__}")

    for k, v in data.items():
        setattr(model, k, v)

    model.save()

def populate_db():

    firms_data = []

    params = dict(view='Grid view')

    response = requests.get(f'https://api.airtable.com/v0/{app_key}/General Firm',
                            headers=headers, params=params).json()

    while 'offset' in response:

        params.update({'offset': response['offset']})

        firms_data += response['records']

        response = requests.get(f'https://api.airtable.com/v0/{app_key}/General Firm',
                                headers=headers, params=params).json()

    firms_data += response['records']

    for firm_data in firms_data:

        id = firm_data['id']
        fields = firm_data['fields']

        data = dict(
            firm_name = fields['Firm Name'] if 'Firm Name' in fields else None,
            year_founded = fields['Year Founded'] if 'Year Founded' in fields else None,
            address = fields['Office Address'] if 'Office Address' in fields else None,
            website = fields['Website'] if 'Website' in fields else None,
            aum = fields['AUM'] if 'AUM' in fields else None,
            size = fields['Size'] if 'Size' in fields else None,
            specialisation = fields['Detailed Firm Specialisations'] if 'Detailed Firm Specialisations'
                                                                        in fields else None,
        )

        firm, _ = Firm.objects.get_or_create(airtable_id=id)
        update_attrs(firm, data)

        if 'Employees' in fields:
            for employee_id in fields['Employees']:
                employee_response = requests.get(
                    f'https://api.airtable.com/v0/{app_key}/Employment History/{employee_id}', headers=headers
                ).json()

                person_id = employee_response['fields']['Person ID'][0] if 'Person ID' in employee_response['fields'] \
                    else None

                if person_id:
                    person_response = requests.get(
                    f'https://api.airtable.com/v0/{app_key}/People/{person_id}', headers=headers
                ).json()

                    id = person_response['id']
                    fields = person_response['fields']

                    data = dict(
                        firm=firm,
                        first_name = fields['First Name'] if 'First Name' in fields else None,
                        last_name = fields['Last Name'] if 'Last Name' in fields else None,
                        gender = fields['Gender'] if 'Gender' in fields else None

                    )

                    employee, _ = Employee.objects.get_or_create(airtable_id=id)
                    update_attrs(employee, data)

                    id = employee_response['id']
                    fields = employee_response['fields']
                    job_id = fields['Job Title'][0] if 'Job Title' in fields else None
                    job_title = None

                    job, _ = Job.objects.get_or_create(airtable_id=id)

                    if job_id:
                        job_response = requests.get(f'https://api.airtable.com/v0/{app_key}/Positions/{job_id}',
                                                    headers=headers
                                                    ).json()

                        job_title = job_response['fields']['Job Title'] if 'Job Title' in job_response['fields'] else None

                    data = dict(
                        employee=employee,
                        title = job_title,
                        investment_lookup = fields['Investment lookup'][0] if 'Investment lookup' in fields else None,
                        start_month = fields['Start Month'] if 'Start Month' in fields else None,
                        end_month = fields['End Month'] if 'End Month' in fields else None,
                        start_year = fields['Start Year'] if 'Start Year' in fields else None,
                        end_year = fields['End Year'] if 'End Year' in fields else None,
                        is_current = fields['Current Role'] if 'Current Role' in fields else None,
                        ic_member = None
                    )

                    update_attrs(job, data)


populate_db()
