from django.test import TestCase
from .models import Student
import datetime
from forms import StudentForm
from django.urls import reverse
from django.test import Client
client = Client()



# Create your tests here.
class StudentTestCase(TestCase):
	def setUp(self):
		self.student = Student(
			first_name = "Cynthia",
			last_name = "Anyango",
			date_of_birth = datetime.date(1996, 9, 11),
			gender = "Female",
			registration_number = "SCT211-0002/2017",
			email = "anyangoc55@gmail.com",
			phone_number = "0746574811",
			date_joined = datetime.date.today(),
		)

	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name, self.student.full_name())    

	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name, self.student.full_name()) 


class CreateStudentTestCase(TestCase):
	def setUp(self):
		self.data = {
			"first_name" : "Nikki",
			"last_name ": "Antonine",
			"date_of_birth ": datetime.date(2006, 12, 12),
			"gender" : "Female",
			"registration_number ":"SCT211-0004/2017",
			"email ": "antonine@gmail.com",
			"phone_number ":"0742528493",
			"date_joined ":datetime.date.today(),
		}

		def test_student_form_accepts_valid_data(self):
			form =  StudentForm(self.data)
			self.assertTrue(form.is_valid())


		def test_student_form_rejects_invalid_data(self):
			form = StudentForm(self.data)


		def test add student view(self):
			client=Client()
			url=reverse("add student")
			request=client.post(url,self.data)
			self.assertEqual(request.status code,200)

		def test add student view rejects bad(self):
			client=Client()
			url=reverse("add student")
			request=client.post(url,self.bad data)
			self.assertEqual(request.status code,400)

		def test_age_above_18(self):
			self.assertFalse(self.student.clean()<18)

		 def test_age_above_18(self):
			self.assertFalse(self.student.clean()>30)



			