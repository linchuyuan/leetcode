#Given a array find a,b,c and d such that a+b+c+d = target

def four_sum_closest(array,target):
	best_set = [array[0],array[1],array[2],array[3]]
	distance = abs(array[0]+array[1]+array[2]+array[3] - target);
	for k in range(len(array)-3):
		num1 = array[k];
		num2 = array[k+1];
		num3 = array[k+2];
		num4 = array[k+3];
		found = True;
		for i in range(len(array)):
			i = array[i]
			indicator = 0;
			if not distance:
				break;
			if abs(i + num2 + num3 + num4 - target) <= distance:
				indicator = 1;
				distance = abs(i + num2 + num3 + num4 - target);
			if abs(i + num1 + num3 + num4 - target) <= distance:
                                indicator = 2;
                                distance = abs(i + num1 + num3 + num4 - target);
			if abs(i + num2 + num1 + num4 - target) <= distance:
                                indicator = 3;
                                distance = abs(i + num2 + num1 + num4 - target);
			if abs(i + num2 + num3 + num1 - target) <= distance:
                                indicator = 4;
                                distance = abs(i + num2 + num3 + num1 - target);
			if indicator == 1:
				num1 = i;
			elif indicator == 2:
				num2 = i;
			elif indicator == 3:
				num3 = i;
			elif indicator == 4:
				num4 = i;
			else: found = False;
		if found:
			best_set = [num1,num2,num3,num4];
			
	return best_set

print four_sum_closest([1,2,3,4,5,6,7],100);


