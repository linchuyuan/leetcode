#Divide two integer without using multiplication,division and mod

def divide(a,b):
	if b == 0:
		return False;
	return_me = 0;
	while a-b > 0:
		a = a - b;
		return_me = return_me + 1;
	return  return_me
print divide(10,3);	
