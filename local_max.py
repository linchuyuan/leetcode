#A peak element is an element that is greater than its neighbors.

#Given an input array where num[i] . num[i+1], find a peak element and return its index.

#The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

#You may imagine that num[-1] = num[n] = -..

#For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.


import time
def local_max(a):
	start = 0;
	end = len(a)-1;
	while start != end:
		if start == end - 1:
			if (a[start] < a[end]):
				return end;
			else:
				return start;
		mid = (end - start)/2;
		print start,mid,end;
		if a[mid] < a[mid+1]:
			start = mid+1;
		elif a[mid] < a[mid-1]:
			end = mid-1 ;
		else:
			return mid;

a = [1,2,3,4,5,4,3,2,6,7,8]
print local_max(a);
