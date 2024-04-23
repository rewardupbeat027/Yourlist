from django.test import TestCase


class SimpleTests(TestCase):
    def test_main_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
