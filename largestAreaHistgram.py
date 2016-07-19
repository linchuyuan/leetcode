#find largest area in histgram
#[2,1,5,6,2,3] -> 10

def largestAreaHistgram(hist):
	stack = list();
	area = 0;
	i = 0;
	while i < len(hist):
		print area
		if len(stack) == 0 or hist[stack[-1]] <= hist[i]:
			stack.append(i);
			i += 1;
		else:
			left = stack.pop();
			area = max(area, hist[left] * (i - left));
	while len(stack) != 0:
		left = stack.pop();
		area = max(area, hist[left] * (i - left));
				
	return area;

a = [2,1,5,6,2,3]
print largestAreaHistgram(a);
