#find depth of binary tree

class binaryTree():
        class node():
                def __init__ (self, data):
                        self.data = data;
                        self.right = None;
                        self.left = None;

        def __init__ (self,data):
                self.root = self.node(data);
	def add(self,data):
		stack = [self.root];
		while len(stack) != 0:
			root = stack.pop(0);
			if root.left == None: 
				root.left = self.node(data); 
				return;
			elif root.right == None: 
				root.right = self.node(data);
				return;
			else: 
				stack.append(root.left); 
				stack.append(root.right);

def binaryThreeDepth(root):
	stack1 = list();
	stack2 = list();
	depth = 0;
	workingIndicator = 1
	stack1.append(root);
	while len(stack1) != 0 or len(stack2) != 0:
		if workingIndicator == 1:
			node = stack1.pop();
			if node.left: stack2.append(node.left);
			if node.right: stack2.append(node.right);
		else:
			node = stack2.pop();
			if node.left: stack1.append(node.left);
                        if node.right: stack1.append(node.right);
		if workingIndicator == 1 and len(stack1) == 0:
			depth += 1;
			workingIndicator = 2;
		elif workingIndicator == 2 and len(stack2) == 0:
                        depth += 1;
                        workingIndicator = 1;
	return depth ;
		


a = binaryTree(1)
a.add(2);
a.add(3);
a.add(4);
a.add(5);
a.add(6);
a.add(7);
a.add(8);
a.add(9);
#print a.root.left.left.left.data
print binaryThreeDepth(a.root);

