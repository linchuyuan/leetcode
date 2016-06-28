#Given a array of S of n intergers. find three intergers in s such that the sum of the three is closest to the target. i.e. [-1,2,1,4] target = 1, return [-1,2,1]
def three_sum_to_zero(array):
	for k in range(len(array)-2):
		num1 = array[k];
		num2 = array[k+1];
		num3 = array[k+2];
		return_me = [];
		distance = num1+num2+num3;
		found = False;
		for i in range(len(array)):
			if i == k:
				continue;
			i = array[i];
			indicator = 0;
			if not distance:
				found = True;
				break;
			if abs(i+num2+num3) < distance:
				indicator = 1;
				distance = abs(num1+i+num3);
			if abs(num1+i+num3) < distance:
				indicator = 2;
				distance = abs(i+num2+num3);
			if abs(num1+num2+i) < distance:
				indicator = 3;
				distance = abs(i+num2+num3);
			if indicator == 1: num1 = i;
			elif indicator == 2: num2 = i;
			elif indicator == 3: num3 = i;
	
		if found:
			return_me.append(num1);
			return_me.append(num2);
			return_me.append(num3);
			continue;
		else:
			return_me = "not found";
	return return_me

print three_sum_to_zero([1,-2,-2,4])
