#rotate a array of size n by b

def rotate_array_1b1(a,b):
	if a == None:
		return a;
	for i in range(b):
		temp_hold = a[-1]; 
		for k in range(len(a)):
			position = k - 1;
			a[k-1] = a[k];
		a[-2] = temp_hold;
	return a;

def rotate_array(a,b):
	if a == None:
		return a;
	for i in range(b):
		k = 0;
		temp_hold = a[i];
		while k < len(a)-1:
			if i+b+k < len(a):
				a[i+k] = a[i+b+k];
			else:
				a[i+k] = a[-1];
			k += b;
		a[-b+i] = temp_hold;
		print a
	
	return a;


a = [1,2,3,4]
print rotate_array(a,2);
			
		
