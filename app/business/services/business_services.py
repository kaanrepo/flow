from business.models import Employee, Team, Customer
from business.serializers import EmployeeSerializer, TeamSerializer, CustomerSerializer

class EmployeeService():

    @staticmethod
    def get_all_employees():
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return serializer.data

    @staticmethod
    def get_employee_by_id(id):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee)
        return serializer.data
    
    @staticmethod
    def create_employee(data):
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None
    
    @staticmethod
    def delete_employee(employee):
        employee.delete()

    @staticmethod
    def update_employee(employee, data):
        serializer = EmployeeSerializer(employee, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None
    
class TeamService():

    @staticmethod
    def get_all_teams():
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return serializer.data
    
    @staticmethod
    def get_team_by_id(id):
        team = Team.objects.get(id=id)
        serializer = TeamSerializer(team)
        return serializer.data
    
    @staticmethod
    def create_team(data):
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None
    
    @staticmethod
    def delete_team(team):
        team.delete()
    
    @staticmethod
    def update_team(team, data):
        serializer = TeamSerializer(team, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None
    
class CustomerService():

    @staticmethod
    def get_all_customers():
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return serializer.data
    
    @staticmethod
    def get_customer_by_id(id):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return serializer.data
    
    @staticmethod
    def create_customer(data):
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None
    
    @staticmethod
    def delete_customer(customer):
        customer.delete()

    @staticmethod
    def update_customer(customer, data):
        serializer = CustomerSerializer(customer, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return None