def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(20,4))

def gdc_extended(x, y):
	while x!=0 and y!= 0:
		if x >= y:
			x -= y
		else:
			y -= x
	return x + y

print(gdc_extended(72,12))