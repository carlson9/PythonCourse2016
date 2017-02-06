#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def gc_divisor(n1, n2):
	while n2 != 0:
		(n1, n2) = (n2, n1%n2)
	return abs(n1)

# gc_divisor (108, 30)
# gc_divisor (6, 30)
# gc_divisor (-6, 30)
# gc_divisor (-6, -30)

	
#Exercise 2
#Write a function that returns prime numbers less than 121
########## THIS DID NOT WORK ################
def primeN (number):
    primes = []
	if number > 2: 
		list = [2, n+1]
		n = [0, len(list)+1]
		for item in list:
			 if item % list[n] == 0:
				continue
			 else: 
				item % list[n+1] != 0
				prime_list.append(item)
		return prime_list
	else: print "All numbers less than 2 are not prime"
	
	
# primeN(1)	
# primeN(7)	

n = 5
 2,  3,   4,   5
 i, i+1, i+2, i+3
	
	3%2 != 0
	i+1 % i != 0
	prime_list.append(i+1)
	
		4%2 == 0
		Drop 4
		i+2 % i ==0
	
	
	

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



