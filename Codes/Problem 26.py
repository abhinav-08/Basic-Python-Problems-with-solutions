def isPrime(n) :
	if (n<=1) :
		return False
	if (n<=3) :
		return True
	x = True    
	for i in range(2,n-1) : 
		if (n%i == 0) :
			x=False
	return x


if (isPrime(11)):
	print("True")
else:
	print("False")