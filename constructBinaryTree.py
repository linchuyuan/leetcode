#given inorder traverval array, construct the tree

class binaryTree():
	class node():
		def __init__(self, data):
			self.data = data;
			self.right = None;
			self.left = None;
	def __init__(self,data):
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
	

def inorderConstruct(array):
	if len(array) == 0:
		return;
	high = len(array) -1;
	low = 0;
	mid = low + (high - low) /2
	bt = binaryTree.node(array[mid]);
	if len(array) == 1:
		return bt;
	bt.left = inorderConstruct(array[:mid]);
	bt.right = inorderConstruct(array[mid+1:]);
	return bt;
def postOrderconstruct(array):
	if len(array) == 0 :
		return;
	bt = binaryTree.node(array[-1]);
	if len(array) == 1:
		return bt;
	half = len(array) / 2;
	bt.left = postOrderconstruct(array[0:half]);
	bt.right = postOrderconstruct(array[half:len(array)-1]);
	return bt;

a = [1,2,3,4,5,6,7]
b = [1,3,2,5,7,6,4]
bt = postOrderconstruct(b);
print	bt.left.right.data
	
