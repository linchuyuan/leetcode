#Given n pairs of parentheses, write a function to generate all combination of parentheses

def generateParentheses(n):
	rst = [];
	getPair(rst,"",n,n);
	return rst;
def getPair(rst,s,left,right):
	print rst,s,left,right;
	if left > right or left < 0 or right < 0: return
	if left == 0 and right == 0:
		rst.append(s);
		return;
	getPair(rst,s+"(",left-1,right);
	getPair(rst,s+")",left,right-1);


n = 2
print generateParentheses(n);
