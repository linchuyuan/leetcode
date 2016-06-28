#given two binary string, return the sum

def add_binary(arg1,arg2):
	up = 0;
	result = "";
	length_diff = len(arg1) - len(arg2);
	if length_diff < 0:
		for i in range(abs(length_diff)):
			arg1 = "0" + arg1;
	elif length_diff > 0:
		for i in range(length_diff):
			arg2 = "0" + arg2;
	length = len(arg1);
	length_list = range(length);
	length_list.reverse();
	print arg1,arg2
	for i in length_list:
		if arg1[i] == "1" and arg2[i] == "1" and up == 1:
			result =  "1" + result;
			up = 1;
		elif arg1[i] == "1" and arg2[i] == "1" and up == 0:
			result = "0" + result;
			up = 1;
		elif arg1[i] == "1" and arg2[i] == "0" and up == 1:
			result = "0" +  result;
			up = 1;
		elif arg1[i] == "1" and arg2[i] == "0" and up == 0:
                        result = "1" + result;
                        up = 0;
		elif arg1[i] == "0" and arg2[i] == "1" and up == 1:
                        result = "0" + result;
                        up = 1;
		elif arg1[i] == "0" and arg2[i] == "1" and up == 0:
                        result = "1" + result;
                        up = 0;
		elif arg1[i] == "0" and arg2[i] == "0" and up == 1:
                        result = "1" + result;
                        up = 0;
		elif arg1[i] == "0" and arg2[i] == "0" and up == 0:
                        result = "0" + result;
                        up = 0
	if up == 1: result = "1" + result;
	return result;


print add_binary("111","1111111111111011111111111111111111111111111111111111111111111111111111111111111");



