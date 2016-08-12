import unittest
from lab3 import *

class labTests(unittest.TestCase):
	
	# for shout()
	def test_shout(self):
 		self.assertEqual('!!!MY NAME IS!!!', shout('My name is'))
 		self.assertNotEqual('my name is', shout('My name is'))
 		with self.assertRaises(NotTextException): shout(1)
 	
	#for reverse()	
 	def test_reverse(self):
 		self.assertEqual('si eman yM', reverse('My name is'))
		with self.assertRaises(NotTextException): reverse(1)
		
	#for reverse_words()
 	def test_reversewords(self):
 		self.assertEqual("is name My", reversewords('My name is'))
 		with self.assertRaises(NotTextException): reversewords(1)
		with self.assertRaises(MoreWordsException): reversewords('My')
			
	#for reverse_wordsletters() 	
  	def test_reversewordletters(self):
  		self.assertEqual('yM eman si', reversewordletters('My name is'))
   		with self.assertRaises(NotTextException): reversewordletters(1)
		with self.assertRaises(MoreWordsException): reversewordletters('My')
	
	#for piglatin()
  	def test_piglatin(self):
 		self.assertEqual('yMay amenay isyay ikavay', piglatin('My name is'))
 		self.assertNotEqual('My name is', piglatin('My name is'))
		with self.assertRaises(NotTextException): piglatin(1)
 
 if __name__ == '__main__': #Add this if you want to run the test with this script.
   unittest.main()