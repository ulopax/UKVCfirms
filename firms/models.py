from django.db import models
import datetime

# Create your models here.


class Firm(models.Model):

    airtable_id = models.CharField(max_length=128)
    firm_name = models.CharField(max_length=128, null=True, blank=True)
    year_founded = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=1028, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    aum = models.CharField(max_length=128, null=True, blank=True)
    size = models.CharField(max_length=32, null=True, blank=True)
    specialisation = models.CharField(max_length=1028, null=True, blank=True)


class Employee(models.Model):

    firm = models.ForeignKey(Firm, null=True, related_name='employees', on_delete=models.CASCADE)
    airtable_id = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=32, null=True, blank=True)

    @property
    def current_job(self):
        return self.jobs.filter(is_current=True).first()

    @property
    def start_date(self):
        if self.current_job:
            if self.current_job.start_year or self.current_job.start_month:
                return f"{self.current_job.start_month}/{self.current_job.start_year}"

        return None


class Job(models.Model):

    employee = models.ForeignKey(Employee, null=True, related_name='jobs', on_delete=models.CASCADE)
    airtable_id = models.CharField(max_length=128)
    title = models.CharField(max_length=256, null=True, blank=True)
    investment_lookup = models.CharField(max_length=256, null=True, blank=True)
    start_month = models.IntegerField(null=True, blank=True)
    end_month = models.IntegerField(null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    is_current = models.BooleanField(default=False, null=True)
    ic_member = models.CharField(max_length=1024, null=True, blank=True)