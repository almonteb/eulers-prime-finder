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
        self.assertIsNone(data[0]['error'])
        self.assertEqual(1, data[0]['xth'])
        self.assertEqual(1, data[0]['num_digits'])
        self.assertEqual(2, data[0]['prime'])
        self.assertEqual(0, data[0]['pos'])

    def test_single_api_fail(self):
        resp = self.app.post('/single', data=json.dumps({'x': 6, 'y': 20}), content_type='application/json')
        self.assertEqual(200, resp.status_code)
        data = json.loads(resp.get_data(as_text=True))
        self.assertEqual(6, data[0]['xth'])
        self.assertEqual(20, data[0]['num_digits'])
        self.assertIsNone(data[0]['prime'])
        self.assertIsNone(data[0]['pos'])
        self.assertEqual('20 digits is too computationally expensive, try a bit lower', data[0]['error'])

    def test_process_bad_x(self):
        prime = app.process_primes(({'xth': 'a', 'num_digits': 1},))[0]
        self.assertEqual('a', prime.xth)
        self.assertEqual(1, prime.num_digits)
        self.assertIsNone(prime.prime)
        self.assertIsNone(prime.pos)
        self.assertEqual('a is an invalid value for X', prime.error)

    def test_process_bad_y(self):
        prime = app.process_primes(({'xth': 2, 'num_digits': 'x'},))[0]
        self.assertEqual(2, prime.xth)
        self.assertEqual('x', prime.num_digits)
        self.assertIsNone(prime.prime)
        self.assertIsNone(prime.pos)
        self.assertEqual('x is an invalid value for Y', prime.error)

    def test_process_large_y(self):
        prime = app.process_primes(({'xth': 2, 'num_digits': 100},))[0]
        self.assertEqual(2, prime.xth)
        self.assertEqual(100, prime.num_digits)
        self.assertIsNone(prime.prime)
        self.assertIsNone(prime.pos)
        self.assertEqual('100 digits is too computationally expensive, try a bit lower', prime.error)

if __name__ == '__main__':
    unittest.main()
