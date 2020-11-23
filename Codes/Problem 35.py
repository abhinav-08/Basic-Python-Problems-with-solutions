def ings(s) :
	l = len(s)
	if ( l<3 ) :
		pass
	elif ( s[-3:] == "ing" ) :
		s = s + "ly"
	else :
		s = s + "ing"
	return s	
	

print(ings("jh"))
