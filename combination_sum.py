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


a = [7,6,3,2];
print combination_sum(a,8);

