#[3,30,34,5,9] -> 9534330

def largestNumber(a):
	rst = str(a[0]);
	for i in a[1:]:
		addOne = str(i);
		k = 0;
		if len(rst) > len(addOne):
			addOneTempHold = addOne + (len(rst)-len(addOne)) * addOne[-1];
			rstTempHold = rst;
		else:
			rstTempHold = rst + (len(addOne) - len(rst)) * rst[-1];
			addOneTempHold = addOne;
		while k < len(rstTempHold):
			if addOneTempHold[k] == rstTempHold[k]:
				k += 1;
				continue;
			if addOneTempHold[k] > rstTempHold[k]:
				rst = addOne + rst;
				break;
			elif addOneTempHold[k] < rstTempHold[k]:
				rst = rst + addOne;
				break;
	return rst

a = [3,30,34,5,9]
print largestNumber(a);
				
