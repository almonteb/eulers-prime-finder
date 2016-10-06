import input_util
import unittest
from ddt import ddt, data
from responses import InvalidUsage


@ddt
class InputUtilTest(unittest.TestCase):
    @data('1', '100', 1, 100)
    def test_intify(self, val):
        self.assertEqual(int(val), input_util.intify(val))

    @data('test', None, '')
    def test_intify_fail(self, val):
        with self.assertRaises(InvalidUsage):
            input_util.intify(val)

    @data(1, 2, 3, 10, 12)
    def test_assert_valid_num_digits(self, num):
        input_util.assert_valid_num_digits(num)

    @data(13, 100)
    def test_assert_valid_num_digits_fail(self, num):
        with self.assertRaises(InvalidUsage):
            input_util.assert_valid_num_digits(num)


if __name__ == '__main__':
    unittest.main()
