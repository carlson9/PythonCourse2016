def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: 
	return '0'
  digits = []
  while num > 0:
	if num % 2 == 1 : 
		digits.append('1')    
	else:
		digits.append('0')
	num /= 2
  return ''.join(digits[::-1])
  
  
  
  
def int_to_base(num, base):
  #"""convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  while num:
        digits.append(str(num % base))
        num /= base
  return digits[::-1]

  
  
def base_to_int(string, base):
  #"""take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  mysum=0
  for i in range(0,len(string)):
	mysum+=base**i*int(string[len(string)-i-1])
  return mysum
  
    

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  int1 = base_to_int(str1, base1)
  int2 = base_to_int(str2, base2)
  tmp = int(int1)+int(int2)
  result = int_to_base(tmp, base1)
  return result 

  def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  int1 = base_to_int(str1, base1)
  int2 = base_to_int(str2, base2)
  tmp = int1+int2
  result = int_to_base(tmp, base1)
  return result
  
  #flexibase_add ('1011','1101',2,2)
  
def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  int1 = base_to_int(str1, base1)
  int2 = base_to_int(str2, base2)
  tmp = int1*int2
  result = int_to_base(tmp, base1)
  return result 

  
  
def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.