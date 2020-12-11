import unittest
import sys
import pathlib
module_path_obj = pathlib.Path(r"D:/Max's Documents/Python projects/FoxM_mentoring/Task 2 Unit tests/anagrams/")
sys.path.append(str(module_path_obj))
from anagrams import *

typical_param = [
	("abcd efgh", "dcba hgfe"),
	("a1bcd efg!h", "d1cba hgf!e"),
	("", ""),
	("123 456", "123 456"), #  added case for numerals only
]


class TestAnagrams(unittest.TestCase):

	def test_typical(self):
		# self.assertEqual(reverse("a1bcd efg!h"), "d1cba hgf!e", "wrong result processing valid string")  # using parameterized tests instead
		for inp_val, ret_val in typical_param:
			with self.subTest():
				self.assertEqual(ret_val, reverse(inp_val))

	def test_atypical(self):
		n: int = 123 #  integer type
		self.assertRaises(TypeError, reverse, n)


if __name__ == '__main__':
	unittest.main()