from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher





class Student Course Test Case(TestCase)
	def setUp(self):

		self.student a = Student.objects.create(
			first_name = "Megg",
            last_name = "Nyakeno",
            date_of_birth = datetime.date(1996, 9, 11),
            gender = "Female",
            registration_number = "SCT211-0002/2017",
            email = "anyangoc55@gmail.com",
            phone_number = "0746574811",
            date_joined = datetime.date.today(),
			)
		

		self.student b = Student.objects.create(first_name = "Antonine",
            last_name = "Nyaoke",
            date_of_birth = datetime.date(1996, 9, 11),
            gender = "Female",
            registration_number = "SCT301-0002/2017",
            email = "antonine@gmail.com",
            phone_number = "0742528493",
            date_joined = datetime.date.today(),)
		

		self.python = Course(
			name= "Python", 
            duration_in_months= 10,
            Course_number= "1001",
            description= "Django and Flask frameworks")
			
		
		self.javascript  = Course(
			name= "javascript", 
            duration_in_months= 10,
            Course_number= "1001",
            description= "Django and Flask frameworks")
		
		
		
		self.hardware  = Course(name= "hardware", 
            duration_in_months= 10,
            Course_number= "1001",
            description= "Django and Flask frameworks")
		

		self.teacher = Teacher(
			first_name="Kelly",
			last_name = "Murugi",
          	place_of_residence = "Nairobi",  
         	gender = "Female",
          	registration_number ="SCT211-0004/2017",
          	email = "kellym@gmail.com",
          	phone_number ="0742528493",
          	date_joined = datetime.date.today(),
			
			)

		def test_student_can_join_many_courses(self):
			self.assertEqual(self.student_a.courses.count(),0)
			self.student_a.courses.add(self.python)
			self.assertEqual(self.student_a.courses.count(),1)
			self.student_a.courses.add(self.javascript)
			self.assertEqual(self.student_a.courses.count(),2)
			self.student_a.courses.add(self.hardware)
			self.assertEqual(self.student_a.courses.count(),3)

		def test_course_can_have_many_students(self):
			self.python.students.add(self.student_a, self.student_b)
			self.assertEqual(self.python.students.count(),2)

		
		