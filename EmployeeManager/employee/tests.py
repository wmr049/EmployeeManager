from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from .models import Employee

class TestEmployee(TestCase):
  
  def setUp(self):
      self.employee = mommy.make(Employee, name='Milton Reis',email='wmr049@gmail.com',department='Tecnologia')
      
  def test_employee_creation(self):
      self.assertTrue(isinstance(self.employee, Employee))
      self.assertEquals(self.employee.__str__(), self.employee.name)