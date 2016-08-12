#write a custom exception, then an inclusive test, then write the code for the following functions:

# custom Exceptions
import string
import traceback

class NotTextException(Exception): # inherits from Exception
	def __init__(self, value):
		Exception.__init__(self, 'This is not text!')
    
class MoreWordsException(Exception): # inherits from Exception
	def __init__(self, value):
		Exception.__init__(self, 'There is only one word. I need more words!')


# inclusive test 
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
 		self.assertEqual('yMay amenay isyay', piglatin('My name is'))
 		self.assertNotEqual('My name is', piglatin('My name is'))
		with self.assertRaises(NotTextException): piglatin(1)
 
 if __name__ == '__main__': #Add this if you want to run the test with this script.
   unittest.main()


# functions themselves
def shout(txt):
	if not isinstance(txt, str):
		raise NotTextException(txt)
	else:
		return '!!!' + txt.upper() + '!!!'
		
def reverse(txt):
	if not isinstance(txt, str):
		raise NotTextException(txt)
	else:
		return txt[::-1]
	
def reversewords(txt):
	if not isinstance(txt, str):
		raise NotTextException(txt)
	if " " not in txt:
		raise MoreWordsException(txt)
	else:
		words = txt.split()
		return ' '.join(reversed(words))
  
  
def reversewordletters(txt):
	if not isinstance(txt, str):
		raise NotTextException(txt)
	if " " not in txt:
		raise MoreWordsException(txt)
	else:
		letters = txt.split()
		output = []
		for letter in letters:
			output.append(reverse(letter))
		return ' '.join(output)
 
 
def piglatin(txt):
	if not isinstance(txt, str):
		raise NotTextException(txt)
	else:
		words = txt.split()
		vowels = ['a', 'o', 'e', 'i', 'u'] 
		output = []
		for word in words:
			first_letter = list(word)[0]
			if first_letter in vowels:
				word += 'yay' #traditional piglatin rule accordsing to Wikipedia
			else:
				word = (word[1:] + first_letter + 'ay')
			output.append(word)
		return ' '.join(output)
