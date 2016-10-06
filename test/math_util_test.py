import unittest
import math_util
from ddt import ddt, data, unpack
from responses import InvalidUsage


@ddt
class MathUtilTest(unittest.TestCase):
    @data((2, 7, 6028747, 20),
          (3, 3, 523, 15),
          (4, 5, 24977, 33),
          (5, 12, 738132328627, 157),
          (10, 9, 675092447, 233),
          (7, 6, 630353, 70))
    @unpack
    def test_find_xth_prime(self, xth, num_digits, prime, pos):
        p = math_util.find_xth_prime(xth, num_digits)
        self.assertEqual(p.xth, xth)
        self.assertEqual(p.num_digits, num_digits)
        self.assertEqual(p.prime, prime)
        self.assertEqual(p.pos, pos)

    @data((2000, 2),)
    @unpack
    def test_find_xth_prime_fail(self, xth, num_digits):
        with self.assertRaises(InvalidUsage):
            math_util.find_xth_prime(xth, num_digits)

    @data(1, 2, 3, 5, 7, 353, 24709, 3232862794349, 7099983170353)
    def test_is_prime(self, num):
        self.assertTrue(math_util.is_prime(num))

    @data(4, 6, 10, 2002, 900000000)
    def test_is_not_prime(self, num):
        self.assertFalse(math_util.is_prime(num))


if __name__ == '__main__':
    unittest.main()
