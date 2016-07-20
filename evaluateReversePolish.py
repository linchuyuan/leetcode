#["2","1","+","3","*"] -> ((2+1)*3) -> 9

def evaReversePolishNotation(l):
	operand1 = None;
	operand2 = None;
	for i in l:
		if i.isdigit():
			if not operand1:
				operand1 = int(i);
			else:
				operand2 = int(i);
		else:
			if i == "/":
				operand1 = operand1 / operand2;
			if i == "*":
				operand1 = operand1 * operand2;
			if i == "+":
				operand1 = operand1 + operand2;
			if i == "-":
				operand1 = operand1 - operand2;
	return operand1; 

a = ["2","1","+","3","*"]
print evaReversePolishNotation(a);
