#Divide two integer without using multiplication,division and mod

def divide(a,b):
	negative = False;
	if b == 0:
		return False;
	if a < 0 or b < 0:
		negative = True;
		if a < 0: a = 0 - a;
		else: b = 0 - b;	
	return_me = 0;
	while a-b > 0:
		a = a - b;
		return_me = return_me + 1;
	if negative:
		return_me = 0 - return_me;
	return return_me;
print divide(-10,3);	
