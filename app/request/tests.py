from django.test import TestCase
from rest_framework.test import APIClient
from request.models import Request
from business.models import Employee
from accounts.models import User



class RequestTestCase(TestCase):

    def setUp(self):

        self.client = APIClient()

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
            duration_type='half day',
            status='pending'
        )

        self.approved_request = Request.objects.create(
            type='holiday',
            requested_by=self.agent_employee,
            reviewed_by=self.coordinator_employee,
            start_date='2020-01-01',
            end_date='2020-01-02',
            description='test description',
            duration_type=1,
            status='approved'
        )


    def test_create_request(self):
        self.client.force_authenticate(user=self.test_agent_user)
        response = self.client.post(
            '/api/v1/requests/',
            {
                'type': 'holiday',
                'requested_by': self.agent_employee.pk,
                'start_date': '2020-01-01',
                'end_date': '2020-01-02',
                'description': 'test description',
                'duration_type': 'full day',
                'status': 'pending'
            }
        )
        self.assertEqual(response.status_code, 201)


    def test_agent_edit_pending_permission(self):
        self.client.force_authenticate(user=self.test_agent_user)
        response = self.client.put(
            f'/api/v1/requests/{self.pending_request.pk}/',
            {
                'type': 'holiday',
                'requested_by': self.agent_employee.pk,
                'start_date': '2020-01-01',
                'end_date': '2020-01-05',
                'description': 'test description',
                'duration_type': 'full day',
                'status': 'pending'
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_agent_edit_approved_permission(self):
        self.client.force_authenticate(user=self.test_agent_user)
        response = self.client.put(
            f'/api/v1/requests/{self.approved_request.pk}/',
            {
                'type': 'holiday',
                'requested_by': self.agent_employee.pk,
                'start_date': '2020-01-01',
                'end_date': '2020-01-03',
                'description': 'test description',
                'duration_type': 'full day',
                'status': 'approved'
            }
        )
        self.assertEqual(response.status_code, 403)
