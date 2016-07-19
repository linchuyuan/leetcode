#return a pointer to the first occurence of needle in haystack

def strStr(s,t):
	i = 0;
	while i < len(s):
		k = 0;
		while k < len(t):
			print i, k
			if s[i] == t[k]:
				i += 1;
				k += 1;
			if k == len(t) - 1:
				return s[(i-len(t)+1):];
			if s[i] != t[k]: break;
		i += 1;	


s = "linchuyuan"
t = "chu"

print strStr(s,t);
