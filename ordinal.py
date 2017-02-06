
# turn an integral into an ordinal


def ordinalFunction(N):
	try:
		N = int(N)
	except TypeError:
		print 'Put in an integer.'
	N = str(N)
	end = {'1':'st', '2':'nd', '3':'rd'}
	if N[-2:-1] == '1': 
		return 'Here is an ordinal: ' + N + 'th'
	if N[-1] in end.keys(): 
		return 'Here is an ordinal: ' + N + end[N[-1]]
	else: return 'Here is an ordinal: ' + N + 'th'