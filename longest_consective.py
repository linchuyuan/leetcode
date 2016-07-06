#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#For example,
#Given [100, 4, 200, 1, 3, 2],
#The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#Your algorithm should run in O(n) complexity.

def longest_consective_string(a):
	ht = {};
	max_length = 0;
	for i in a:
		ht[i] = 0;
	current_length = 1;
	for i in a:
		k = i;
		while True:
			try: 
				ht[k+1];
				current_length = current_length + 1;
				k = k + 1;
				if current_length > max_length:
					max_length = current_length;
			except KeyError:
				current_length = 1;
				break;
	return max_length;

a = [100, 4, 200, 1, 3, 2,5,2,6]
print longest_consective_string(a);
