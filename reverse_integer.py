#reverse integer: 123 => 321; -123 => -321

def reverse_integer(n):
	mod = 1;
	reverse_result = 0;
	start = 1;
	if n < 0:
		negative = True;
		n = n * -1;
	else:
		negative = False;
	length = find_integer_length(n);
	for i in range(length-1):
		mod = mod * 10;
	for i in range(length):
		reverse_result = reverse_result + start * (n / mod);
		n = n - (n / mod) * mod;
		mod = mod / 10;
		start = start * 10;
	if negative:
		return -1 * reverse_result;
	else:
		return reverse_result;


def find_integer_length(n):
	mod = 1;
	length = 1;
	while not (n / mod <= 9 and n / mod >= 0):
		length = length + 1;
		mod = mod * 10;
	return length;


n = -1234567;
print reverse_integer(n);


