#Given a string S and a string T, count the number of distinct subsequences of T in s
#S = "rabbbit"
#T = "rabbit"
#return 3

def distinct_seq(s,t):
	distinct_seq = 0;
	if len(t) > len(s):
		return None;
	start = 0;
	count = 0;
	for i in range(len(s)):
		if s[i] == t[start]:
			start += 1;
		
