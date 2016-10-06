import unittest
import app
import json


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_single_api(self):
        resp = self.app.post('/single', data=json.dumps({'x': 1, 'y': 1}), content_type='application/json')
        self.assertEqual(200, resp.status_code)
        data = json.loads(resp.get_data(as_text=True))
        self.assertEqual(None, data['error'])
        self.assertEqual(1, data['primes'][0]['xth'])
        self.assertEqual(1, data['primes'][0]['num_digits'])
        self.assertEqual(2, data['primes'][0]['prime'])
        self.assertEqual(0, data['primes'][0]['pos'])

    def test_single_api_fail(self):
        resp = self.app.post('/single', data=json.dumps({'x': 6, 'y': 20}), content_type='application/json')
        self.assertEqual(400, resp.status_code)
        data = json.loads(resp.get_data(as_text=True))
        self.assertEqual('20 digits is too computationally expensive, try a bit lower', data['error'])

if __name__ == '__main__':
    unittest.main()
