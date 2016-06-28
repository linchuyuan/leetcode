#implement LRU cache class

class cache():
	class __node():
		def __init__ (self,p,n,value):
			self.p = p;
			self.n = n;
			self.value = value;
			
	def __init__ (self,size):
		self.head = None;
		self.tail = None;
		self.table = {} ;
		self.size = size
	def set(self,key,value):
		if not self.head:
			self.table[key] = self.__node(None,None,value);
			self.tail = self.head = key;
			return True;
		if key in self.table.keys():
			self.remove(key);
			self.add(key,value);
			return True
		if len(self.table) < self.size:
			self.add(key,value);
			return True;
		else:
			self.remove(self.tail);
			self.add(key,value);
	def get(self,key):
		if key not in self.table.keys():
			return False;
		if key == self.head:
			return self.table[key].value;
		else:
			temp = self.table[key].value;
			self.remove(key);
			self.add(key,temp);
			return temp;

	def remove(self,key):
		if self.tail == key:
			self.table[self.tail] = self.table[key].p;
			self.table.pop(key);
			return True;
		if self.head == key:
			self.table[self.head] = self.table[key].n;
			self.table.pop(key);
			return True;
		else:
			a = self.table[key]
			self.table[key].p.n = self.table[key].n;
			self.table[key].n.p = self.table[key].p;
			self.table.pop(key);
                        return True;
	def add(self,key,value):
		self.table[key] = self.__node(None,self.table[self.head],value);
                self.table[self.head].p = self.table[key];
                self.head=key;

c = cache(2);
c.set("1","lin");
c.set("2","chu");
c.set("3","yuan");
print c.get("2");
print c.get("3");
print c.get("2");

print c.table,c.head;
