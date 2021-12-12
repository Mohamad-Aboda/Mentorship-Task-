from django.test import TestCase, SimpleTestCase 
from django.urls import reverse, resolve 
from . models import Task 
from .views import task_create_list, task_update_detail_delete


# test views 
class TaskListViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		num_of_tasks = 30
		for task_id in range(num_of_tasks):
			Task.objects.create(title=f"Task Number {task_id}", state="draft")

	def test_url_exists(self):
		response = self.client.get("/api/tasks/")
		self.assertEquals(response.status_code, 200)
		
	def test_url_accessible_by_name(self):
		response = self.client.get(reverse('create_list'))
		self.assertEquals(response.status_code, 200)


	def test_title_content(self):
		task = Task.objects.get(id=1)
		expected_object_name = f'{task.title}'
		self.assertEquals(expected_object_name, 'Task Number 0')


	def test_state_content(self):
		task = Task.objects.get(id = 1)
		expected_object_name = f'{task.state}'
		self.assertEquals(expected_object_name, 'draft')



