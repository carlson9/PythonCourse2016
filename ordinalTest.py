#ordinalTest

import unittest
from ordinal import*

class ordinalTest(unittest.TestCase):
	
	def test_out(self):
		self.assertEqual("1st!!!",ordinalFunction(1))
		self.assertEqual("2nd!!!",ordinalFunction(2))
		self.assertEqual("3rd!!!",ordinalFunction(3))
		self.assertEqual("10th!!!",ordinalFunction(10))
		self.assertEqual("23rd!!!",ordinalFunction(23))
		
		self.assertNotEqual ("1nd!!!", ordinalFunction(1))
		self.assertNotEqual("2rd!!!",ordinalFunction(2))
		self.assertNotEqual("3th!!!",ordinalFunction(3))
		self.assertNotEqual("10st!!!",ordinalFunction(10))
		self.assertNotEqual("23nd!!!",ordinalFunction(23)) 
  
if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()

  
 
  
