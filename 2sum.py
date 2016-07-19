#given a target number find combination sum to the target in the array

def twoSum(a,t):
	a.sort();
	left = 0;
	right = len(a)-1;
	while left <= right:
		rst = a[left] + a[right];
		if rst == t:
			return [a[left],a[right]];
		elif rst > t:
			right -= 1;
		elif rst < t:
			left += 1;
a = [2, 7, 11, 15]
print twoSum(a,9)
