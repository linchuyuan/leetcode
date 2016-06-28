#Returns true if a string is a sub string of the other one 

def substr(base, target):
	if len(target) > len(base):
		return False;
	else:
		i = 0;
		while i < len(base) - len(target) + 1:
			k = 0;
			while k < len(target):
				if target[k] != base[i+k]:
					break;
				k = k + 1;
				if k == len(target) - 1:
					return True;
			i = i +1;
		return False;

print substr("linchuyuan","chuyuan");
