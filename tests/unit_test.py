import unittest
from anagrams.anagrams import *

typical_param = [
	("abcd efgh", "dcba hgfe"),
	("a1bcd efg!h", "d1cba hgf!e"),
	("", ""),
]


class TestAnagrams(unittest.TestCase):

	def test_typical(self):
		# self.assertEqual(reverse("a1bcd efg!h"), "d1cba hgf!e", "wrong result processing valid string")  # using parameterized tests instead
		for p1, p2 in typical_param:
			with self.subTest():
				self.assertEqual(p1, reverse(p2))

	def test_atypical(self):
		self.assertEqual(None, reverse("123"), "Test for entering numbers only")


if __name__ == '__main__':
	unittest.main()
