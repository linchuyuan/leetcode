#convert a integer to roman integer
num_table = [1,4,5,9,10,40,50,90,100,400,500,900,1000];
num_str = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M'];

def int_to_roman(num):
	start_point = 0;
	rep = "";
	for i in range(len(num_table)):
		if num == num_table[i]:
			return num_str[i];
		if num < num_table[i]:
			start_point = i-1;
			break;
	if start_point == 0: start_point = len(num_table)-1;
	rep = num_str[start_point];
	rep_num = num_table[start_point];
	diff = num - rep_num;
	rep = rep + int_to_roman(diff)
	return rep;


num = 39;
print int_to_roman(num);
	
