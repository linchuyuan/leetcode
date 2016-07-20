def binarySearch(a,t,high,low):
	if high == low and a[high] == t:
		return high;
	elif high == low and a[high] != t:
		return False;
	mid =  low + (high - low)/2
	if a[mid] == t:
		return mid;
	elif a[mid] > t:
		return binarySearch(a,t,mid-1,low);
	elif a[mid] < t:
		return binarySearch(a,t,high,mid+1);

a = [1,2,3,4,5]
print binarySearch(a,6,len(a)-1,0);
