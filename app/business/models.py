from django.db import models

BLOOD_TYPE_CHOICES = [
    ("A Rh+", "A Rh+"),
    ("A Rh-", "A Rh-"),
    ("B Rh+", "B Rh+"),
    ("B Rh-", "B Rh-"),
    ("AB Rh+", "AB Rh+"),
    ("AB Rh-", "AB Rh-"),
    ("O Rh+", "O Rh+"),
    ("O Rh-", "O Rh-"),
]

EMPLOYEE_POSITION_CHOICES = [
    ("GM", 'General Manager'),
    ("HR", 'Human Resources'),
    ('TL', 'Team Leader'),
    ('TC', 'Team Coordinator'),
    ('EX', 'Expert'),
    ('AG', 'Agent')
]

TEAM_CHOICES = [
    ('DG1', 'Digital 1'),
    ('DG2', 'Digital 2'),
    ('DG3', 'Digital 3'),
    ('FL', 'First Line'),
    ('FB', 'Flying Blue'),
    ('MI', 'Management Information'),
    ('MG', 'Management'),
    ('OF', 'Office'),
    ('SP', 'Specialist')
]

class Employee(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    position = models.CharField(max_length=4, choices=EMPLOYEE_POSITION_CHOICES, null=True)
    alocation_balance = models.FloatField(null=True, blank=True)
    yearly_allocation = models.FloatField(null=True, blank=True)
    last_allocation_update = models.DateField(null=True, blank=True)
    #team = models.CharField(max_length=4, choices=TEAM_CHOICES, null=True)
    birthday = models.DateField(null=False, blank=False)
    contract_start = models.DateField(null=False, blank=False)
    contract_end = models.DateField(null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    afr_id = models.CharField(max_length=20, null=True, blank=True)
    windows_account_expiry_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=20, null=True, blank=True)
    emergency_contacts = models.TextField(null=True, blank=True)
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPE_CHOICES, null=True, blank=True)
    schengen_visa_status = models.BooleanField(default=False)
    military_service_status = models.BooleanField(default=False)
    safety_certificat_status = models.BooleanField(default=False)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(choices=TEAM_CHOICES, max_length=20)
    leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='leader_of')
    coordinator = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='coordinator_of')
    members = models.ManyToManyField('Employee', related_name='related_team')

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=30)
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    