
class binaryTree():
	class node():
		def __init__ (self, data):
			self.data = data;
			self.right = None;
			self.left = None;

	def __init__ (self,data):
		self.root = node(data);
	def addRight(self,node,data):
		if node.right != None:
			return False;
		else:
			node.right = node(data);
	def addLeft(self,node,data):
		if node.left != None:
                        return False;
                else:
                        node.left = node(data);

	
