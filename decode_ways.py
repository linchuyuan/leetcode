# message containing letters from A-Z is being encoded to numbers using the following mapping:

#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given an encoded message containing digits, determine the total number of ways to decode it.

#For example,
#Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

#The number of ways decoding "12" is 2.

def decode_ways(m):
	ways = [0 for i in range(len(m) + 1)];
	ways[0] = ways[1] = 1
	for i in range(1,len(m)):
		pre = int(m[i-1]) * 10 + int(m[i]);
		if pre <= 26:
			ways[i+1]=(ways[i+1] + ways[i-1])
		else:
			ways[i+1] = (ways[i+1] + ways[i])
	print ways
	return ways[-1];

m = "12";
print decode_ways(m);
