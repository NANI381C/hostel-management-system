from django.test import TestCase
from .models import Student


class DeleteStudentTests(TestCase):
	def test_delete_student_without_room(self):
		student = Student.objects.create(
			name="Roomless Student",
			email="student@example.com",
			phone="1234567890",
			address="Test address",
			college="Test college",
			course="Test course",
			photo="students/test.jpg",
			id_proof="idproof/test.pdf",
		)

		response = self.client.get(f"/students/delete-student/{student.pk}/")

		self.assertEqual(response.status_code, 302)
		self.assertFalse(Student.objects.filter(pk=student.pk).exists())
