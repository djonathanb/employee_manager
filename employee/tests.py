from rest_framework import test, status

from .models import Department, Employee


class EmployeeAPITests(test.APITransactionTestCase):

    def setUp(self):
        self.architecture_department = Department(name='Architecture')
        self.architecture_department.save()

        self.ecomm_department = Department(name='E-commerce')
        self.ecomm_department.save()

        self.mobile_department = Department(name='Mobile')
        self.mobile_department.save()

        self.arnaldo_employee = Employee(
            name='Arnaldo Pereira',
            email='arnaldo@luizalabs.com',
            department=self.architecture_department)
        self.arnaldo_employee.save()

        self.renato_employee = Employee(
            name='Renato Pedigoni',
            email='renato@luizalabs.com',
            department=self.ecomm_department)
        self.renato_employee.save()

        self.catoto_employee = Employee(
            name='Thiago Catoto',
            email='catoto@luizalabs.com',
            department=self.mobile_department)
        self.catoto_employee.save()

    def test_list(self):
        response = self.client.get('/api/employee/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'Arnaldo Pereira')
        department_name = self.architecture_department.name
        self.assertEqual(response.data[0]['department'], department_name)

    def test_get(self):
        url = f'/api/employee/{self.arnaldo_employee.id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Arnaldo Pereira')
        department_id = self.arnaldo_employee.department_id
        self.assertEqual(response.data['department'], department_id)

    def test_create(self):
        employee = {
            'name': 'Djonathan Barros',
            'email': 'djonathan@luizalabs.com',
            'department': self.ecomm_department.id,
        }

        response = self.client.post('/api/employee/', data=employee)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['id'])
        self.assertEqual(response.data['name'], 'Djonathan Barros')

    def test_update(self):
        employee = {
            'name': 'Arnaldo Pereira',
            'email': 'arnaldo.pereira@luizalabs.com',
            'department': self.ecomm_department.id,
        }

        url = f'/api/employee/{self.arnaldo_employee.id}/'
        response = self.client.put(url, data=employee)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated = Employee.objects.get(id=self.arnaldo_employee.id)
        self.assertEqual(updated.id, self.arnaldo_employee.id)
        self.assertEqual(updated.email, 'arnaldo.pereira@luizalabs.com')
        self.assertEqual(updated.department_id, self.ecomm_department.id)

    def test_delete(self):
        url = f'/api/employee/{self.arnaldo_employee.id}/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
