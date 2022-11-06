# test practice.py  

import unittest
import practice

class TestPractice(unittest.TestCase):

	def test_dice(self):
		for x in range(20):		
			roll = practice.dice()
			self.assertTrue( roll >= 3)
			self.assertTrue(roll<= 18)
	def test_2d6(self):
		roll = practice.dice(2)
		self.assertTrue ( roll >= 2)
		self.assertTrue (roll <= 12)

	def test_d100(self):
		roll = practice.dice(1,100)
		self.assertTrue(roll>=1)
		self.assertTrue(roll<=100)



