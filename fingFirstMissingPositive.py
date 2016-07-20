#find the fist missing positive given a unsorted positive array

def findFirstMissingPositive(a):
	for i in a:
		try:
			a[abs(i)-1] = -1 * a[abs(i)-1];
		except:
			continue;
	for i in range(len(a)):
		if a[i] > 0:
			return i+1;

a = [5,1,2,6,3]
print findFirstMissingPositive(a);
