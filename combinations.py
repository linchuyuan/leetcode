# given two integers n and k, return all possible combinations of k numbers out of 1..n

def combination(n,k):
	i = 1;
	rst = [];
	curr = [];
	level = 1;
	combinationDFS(rst,curr,n,k,level);
	return rst
def combinationDFS(rst,curr,n,k,level):
	if len(curr) == k:
		rst.append(list(curr));
		print rst
		return;
	if len(curr) > k:
            return;
	i = level
	while i <= n:
		curr.append(i);
		combinationDFS(rst,curr,n,k,i + 1);
		curr.pop();
		i += 1;

print combination(4,2)
