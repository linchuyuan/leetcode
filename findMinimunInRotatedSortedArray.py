#find minimum in a rotated sorted array

def minimumInRotatedSortedArray(a,high,low):
	if high == low:
		return a[high];
	mid = low + (high - low)/2
	if a[mid] < a[mid+1] and a[mid] < a[mid-1]:
		return a[mid];
	elif a[mid] > a[high]:
		return minimumInRotatedSortedArray(a,high,mid+1);
	elif a[low] > a[mid]:
		return minimumInRotatedSortedArray(a,mid-1,low);
	return a[0];

a = [2,3,4,5,1]
print minimumInRotatedSortedArray(a,len(a)-1,0);
