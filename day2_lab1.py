In the end, you should be able to:

Add a student's name to the roster for a grade
"Add Jim to grade 2."
"OK."
Get a list of all students enrolled in a grade
"Which students are in grade 2?"
"We've only got Jim just now."
Get a sorted list of all students in all grades. Grades should sort as 1, 2, 3, etc., and students within a grade should be sorted alphabetically by name.
"Who all is enrolled in school right now?"
"Grade 1: Anna, Barb, and Charlie. Grade 2: Alex, Peter, and Zoe. Grade 3…"
Note that all our students only have one name. (It's a small town, what do you want?)



class School (object):
	def __init__(self, name):
		self.name = name
		self.roster = {1:[], 2:[], 3:[], 4:[],5:[], 6:[]} #create dictionary
	
	def addStudent(self, name, grade):
		self.roster[grade].append(name)
		print "Added %s to %s grade roster" % (name, grade)
		
	def printRoster(self, grade):
		print  '\n'.join(self.roster[grade])
		
	def __str__ (self):
		output = ''
		for grades in self.roster.keys():
			ouput += 'Grade %d: %s \n' %(grades, str(''.join(sorted(self.roster[grades]))))
		return output
			
	def __repr__(self):
		return self.__str__()
		

washu = School ("Washington University")