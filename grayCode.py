#generate n gray code. e.g. n = 2 -> return [0,1,3,2]

def grayCode(n):
	rst = [0]
	position = 0;
	for i in range(n):
		for k in range(len(rst)):
			rst.append(~k);
	return rst;

print grayCode(3);
		
