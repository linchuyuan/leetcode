#iGiven a set of number and a target number. find all combinations in the set such as the sum is equal to target. the same number can be used for unlimited times

def combination_sum(e,t):
	a = [];
	for i in range(len(e)):
		a.append( c_s(e[i:],t));
	i = 0;
	while i < len(a):
		if a[i] == None:
			a.pop(i);
		else: i = i + 1;
	return a;
		

def c_s (e,t):
	if len(e) == 0:
		return;
	if e[0] > t:
		return c_s(e[1:],t);
	if e[0] <= t and t % e[0] == 0:
		return [e[0] for i in range(t / e[0])];
	else:
		a = c_s(e[1:],t-e[0]);
		if a != None:
			return [e[0]] + a;

def combination_sum_trail2(c,t):
	c = sorted(c);
	return_me = [];
	i = 0
	while i < len(c):
		print c ,t
		if c[i] >= t:
			if c[i] == t:
				return i;
			print "no match"
			return None;
		for k in range(len(c[(i+1):])):
			sub = combination_sum_trail2(c[i+k+1:],t-c[i]);
			if sub:
				return_me.append([c[i],sub]);
		i += 1
	return return_me;
a = [2,3,5,7];
print combination_sum_trail2(a,7);

