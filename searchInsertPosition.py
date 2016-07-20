#iven a sorted array and target value. return the index if found . if not return the index where it should inserted


def searchInsertPosition(a,t):
	high = len(a)-1;
	low = 0;
	mid = low + (high - low) /2
	while high >= low:
		if low >= high: return len(a) ;
        	if high == 0: return 0;
		if a[mid] <= t and a[mid+1] >= t: return mid + 1;
		elif a[mid] >= t and a[mid-1] <= t: return mid -1;
		if a[mid] > t:
			high = mid - 1;
		elif a[mid] < t:
			low = mid + 1;
		elif high == low:
			low += 1;
		mid = low + (high - low)/2


a = [1,2,3]
print searchInsertPosition(a,5);
