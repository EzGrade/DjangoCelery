from django.test import TestCase


# Create your tests here.
class TestAddEndpoint(TestCase):
    def test1(self):
        response = self.client.get('/api/task/')
        result = self.client.get(f'/api/task/result/{response.data["task_id"]}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result.data['result'], 8)
