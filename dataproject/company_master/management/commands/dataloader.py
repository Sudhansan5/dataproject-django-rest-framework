from django.core.management.base import BaseCommand, CommandError
from company_master.models import CompanyData
import csv
import datetime


class Command(BaseCommand):
    '''
    Command to load CSV data
    '''
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        try:
            with open(options['csv_file'], 'r', encoding='latin-1') as file:
                csv_reader = csv.reader(file, delimiter=",")
                row_adder = []
                next(csv_reader)
                for count, row in enumerate(csv_reader):

                    if row[6] == "NA":   # replace NA with Null in table
                        row[6] = None
                    else:
                        row[6] = datetime.datetime.strptime(
                            row[6], '%d-%m-%Y'
                            ).date()

                    row_adder.append(CompanyData(
                        CORPORATE_IDENTIFICATION_NUMBER=row[0],
                        COMPANY_NAME=row[1],
                        COMPANY_STATUS=row[2],
                        COMPANY_CLASS=row[3],
                        COMPANY_CATEGORY=row[4],
                        COMPANY_SUB_CATEGORY=row[5],
                        DATE_OF_REGISTRATION=row[6],
                        REGISTERED_STATE=row[7],
                        AUTHORIZED_CAP=int(float(row[8])),
                        PAIDUP_CAPITAL=int(float(row[9])),
                        INDUSTRIAL_CLASS=row[10],
                        BUSINESS_ACTIVITY=row[11],
                        REGISTERED_OFFICE_ADDRESS=row[12],
                        REGISTRAR_OF_COMPANIES=row[13],
                        EMAIL_ADDR=row[14],
                        LATEST_YEAR_ANNUAL_RETURN=row[15],
                        LATEST_YEAR_FINANCIAL_STATEMENT=row[16]
                    ))

                    if count % 10000 == 0:
                        CompanyData.objects.bulk_create(row_adder)
                        row_adder.clear()

                CompanyData.objects.bulk_create(row_adder)

                self.stdout.write(self.style.SUCCESS(
                        'Data Added'
                        ))
        except IOError:
            raise CommandError("File not found.Please enter correct path")
