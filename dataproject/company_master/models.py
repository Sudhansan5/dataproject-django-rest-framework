from django.db import models

# Create your models here.


class CompanyData(models.Model):
    '''
    Creates table schema
    '''

    CORPORATE_IDENTIFICATION_NUMBER = models.CharField(max_length=250,
                                                       primary_key=True)
    COMPANY_NAME = models.CharField(max_length=250)
    COMPANY_STATUS = models.CharField(max_length=250)
    COMPANY_CLASS = models.CharField(max_length=250)
    COMPANY_CATEGORY = models.CharField(max_length=250)
    COMPANY_SUB_CATEGORY = models.CharField(max_length=250)
    DATE_OF_REGISTRATION = models.DateField(null=True)
    REGISTERED_STATE = models.CharField(max_length=250)
    AUTHORIZED_CAP = models.CharField(max_length=250)
    PAIDUP_CAPITAL = models.CharField(max_length=250)
    INDUSTRIAL_CLASS = models.CharField(max_length=250)
    BUSINESS_ACTIVITY = models.CharField(max_length=250)
    REGISTERED_OFFICE_ADDRESS = models.CharField(max_length=250)
    REGISTRAR_OF_COMPANIES = models.CharField(max_length=250)
    EMAIL_ADDR = models.CharField(max_length=250)
    LATEST_YEAR_ANNUAL_RETURN = models.CharField(max_length=250)
    LATEST_YEAR_FINANCIAL_STATEMENT = models.CharField(max_length=250)

    def __str__(self):
        return self.COMPANY_NAME
