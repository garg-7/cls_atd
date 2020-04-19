from django.db import models
from django_countries.fields import CountryField


class AbstractInformation(models.Model):
    CREDIT_CHOICES = [
        ('1', 'Credit me by name on the site'),
        ('2', 'Do not credit me by name on the site')
    ]
    email_address = models.EmailField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    contribution_credit = models.CharField(max_length=1, choices=CREDIT_CHOICES)
    agreement_and_consent = models.BooleanField()
    country = CountryField()

    class Meta:
        abstract = True


class LegalDecisions(AbstractInformation):
    jurisdiction_within_country = models.TextField(blank=True, null=True)
    court_name = models.CharField(max_length=64)
    decision_location = models.CharField(max_length=64)
    date_of_decision = models.DateField(blank=True)
    link_to_original_decision = models.URLField()
    link_to_english_translation = models.URLField(blank=True)
    background_information = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    result_of_ruling = models.TextField(blank=True, null=True)
    cc_implications = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(blank=True)

    def __str__(self):
        return self.court_name


class LegalScholarship(AbstractInformation):
    title = models.CharField(max_length=64)
    authors = models.CharField(max_length=64, blank=True)
    date_published = models.DateField(blank=True)
    link_to_resource = models.URLField()
    summary = models.TextField()
    is_approved = models.BooleanField(blank=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=128)
    answer = models.TextField()
