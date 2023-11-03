from django.test import TestCase
from request.models import Request
from business.models import Employee
from unittest.mock import patch
from accounts.models import User


class RequestTestCase(TestCase):

    def setUp(self):

        self.test_agent_user = User.objects.create_user(
            username='test agent',
            password='test password',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )
        self.test_agent_user.set_password('test password')

        self.test_expert_user = User.objects.create_user(
            username='test expert',
            password='test password',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        self.test_coordinator_user = User.objects.create_user(
            username='test coordinator ',
            password='test password',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        self.test_teamleader_user = User.objects.create_user(
            username='test teamleader',
            password='test password',
            is_staff=True,
            is_superuser=False,
            is_active=True
        )

        self.agent_employee = Employee.objects.create(
            name='test employee',
            position='AG',
            user=self.test_agent_user
        )
        self.expert_employee = Employee.objects.create(
            name='test employee',
            position='EX',
            user=self.test_expert_user
        )

        self.coordinator_employee = Employee.objects.create(
            name='test employee',
            position='TC',
            user=self.test_coordinator_user
        )

        self.team_lead_employee = Employee.objects.create(
            name='test employee',
            position='TL',
            user=self.test_teamleader_user
        )

        self.pending_request = Request.objects.create(
            type='holiday',
            requested_by=self.agent_employee,
            reviewed_by=None,
            start_date='2020-01-01',
            end_date='2020-01-02',
            description='test description',
            duration=1,
            status='pending'
        )

        self.approved_request = Request.objects.create(
            type='holiday',
            requested_by=self.expert_employee,
            reviewed_by=self.coordinator_employee,
            start_date='2020-01-01',
            end_date='2020-01-02',
            description='test description',
            duration=1,
            status='approved'
        )

    def test_request_create_by_agent(self):
        self.client.force_login(self.test_agent_user)
        response = self.client.post(
            path=f'/api/v1/requests/',
            data={
                'type': 'working from office',
                'requested_by': self.agent_employee.pk,
                'start_date': '2020-01-01',
                'end_date': '2020-01-02',
                'description': 'test description',
                'duration': 'half day',
                'status': 'pending',

            }
        )
        self.assertEqual(response.status_code, 201)

    def test_pending_request_edit_by_agent(self):
        self.client.force_login(self.test_agent_user)
        response = self.client.put(
            path=f'/api/v1/requests/{self.pending_request.uuid}/',
            data={
                'type': 'working from office',
                'requested_by': self.agent_employee.pk,
                'start_date': '2020-01-01',
                'end_date': '2020-01-03',
                'description': 'test description',
                'duration': 'half day',
                'status': 'pending',

            }
        )
        self.assertEqual(response.status_code, 200)
