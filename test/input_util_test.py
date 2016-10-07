import input_util
import unittest
from ddt import ddt, data


@ddt
class InputUtilTest(unittest.TestCase):
    @data('1', '100', 1, 100)
    def test_is_int(self, val):
        self.assertTrue(input_util.is_int(val))

    @data('test', None, '')
    def test_is_int_fail(self, val):
        self.assertFalse(input_util.is_int(val))


if __name__ == '__main__':
    unittest.main()
