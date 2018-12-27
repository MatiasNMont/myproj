
def medium(lister):
	lister.sort()
	print lister
	l = 0
	if len(lister) % 2 == 0:
		l = lister[len(lister)/2] + lister[len(lister)/2 - 1] 
		return float(l/2.0)
	else:
		return lister[len(lister)/2] 
		
		
  



print  medium([5,3,6,4,1]) 
