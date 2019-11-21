from django.test import TestCase
from .models import Teacher
import datetime
from .forms import TeacherForm
from django.urls import reverse
from django.test import Client
client = Client()

class CreateTeacherTestCase(TestCase):
	def setUp(self):
		self.data={
			"first_name":"Kelly",
			"last_name" : "Murugi",
        	"place_of_residence" : "Nairobi",  
            
         	"gender" : "Female",
         	"registration_number ":"SCT211-0004/2017",
         	"email ": "kellym@gmail.com",
         	"phone_number ":"0742528493",
         	"date_joined ":datetime.date.today(),
		}

	self.bad_data ={
			"first_name":"",
			"last_name" : "Murugi",
         	"place_of_residence" : "56789",  
            
         	"gender" : "387575",
          	"registration_number ":"SCT211-0004/2017",
          	"email ": "kellym@gmail.com",
          	"phone_number ":"0742528493",
          	"date_joined ":datetime.date.today(),
	}

	def test_teacher_form_accepts_valid_data(self):
            form =  TeacherForm(self.data)
            self.assertTrue(form.is_valid())

    def test_teacher_form_rejects_invalid_data(self):
            form =  TeacherForm(self.bad_data)
            self.assertFalse(form.is_valid())

     def test_add_teacher_view(self):
            url=  reverse("add_teacher")
            self.assertEqual(request.status_code,200)

     def test_add_teacher_view_rejects_bad_data(self):
            url=  reverse("add_teacher")
            request = client.post(url,self.bad_data)
            self.assertEqual(request.status_code,400)
    

 

# Create your tests here.
