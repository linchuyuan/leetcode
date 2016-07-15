#Given an unsorted integer array, find the first missing positive integer

def find_miss(a):
	ht = {};
	minimun = maximun = a[0];
	for i in a:
		ht[i] = 0;
		if i < minimun: minimun = i;
		if i > maximun: maximun = i;
	for i in a:
		print i, minimun;
		if i == minimun:
			try:
				ht[i+1];
			except KeyError:
				return i+1;
		elif i == maximun:
                        try:
                                ht[i-1];
                        except KeyError:
                                return i-1;
		else:
			try:
				ht[i+1];
			except KeyError:
				return i+1;
			try:
				ht[i-1];
			except KeyError:
				return i-1;
	return True;

a = [1,2,4];
print find_miss(a);
