class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
		if self.minutes < 10:
			return 'The time is  %d:0%d.' % (self.hour, self.minutes)
		else: return 'The time is  %d:%d.' % (self.hour, self.minutes) 
   
  
    def __add__(self, minutes):
		new_minutes = self.minutes + minutes
		new_hour = self.hour + new_minutes/60
        new_minutes2 = new_minutes % 60
	    if new_minutes >9 and new_minutes < 60:
			return 'The new time is %d:%d' %(self.hour, new_minutes)
		elif new_minutes < 10:
            return 'The new time is %d:0%d' %(self.hour, new_minutes)
        else:
            new_minutes > 60
            if new_minutes2 <10:
				return 'The new time is  %d:0%d.' % (new_hour, new_minutes2)
            else: return 'The new time is %d:%d' %(new_hour, new_minutes2)
			



#party_time = Clock (21,1)
#party_time +63
#print party_time   
    def __eq__(self, other):
		if self.hour==other.hour and self.minutes==other.minutes:
			print 'True'
		else:
			print 'False'
			
			
    def __ne__(self, other):
		if self.hour!=other.hour or self.minutes!=other.minutes:
			print 'True'
		else:
			print 'False'
		
############### still need to figure out the sub function	
    def __sub__(self, minutes):
		minutes_r =  minutes % 60
		new_hour =  self.hour - new_minutes/60
		if new_minutes > 9:
			return 'The new time is %d:%d' %(new_hour, new_minutes)
		elif new_minutes < 10 and new_minutes >= 0:
			return 'The new time is %d:0%d' %(new_hour, new_minutes)
		else: 
			new_minutes < 0
			new_hour = minutes/60
			new_minutes2 = new_minutes % 60
			if new_minutes2 <10:
				return 'The new time is  %d:0%d.' % (new_hour, new_minutes2)
			else: return 'The new time is %d:%d' %(new_hour, new_minutes2)
	

			
