class Node: 
 def __init__(self, key, value): 
  self.key = key 
  self.value = value 
  self.next = None


class HashTable: 
 def __init__(self, capacity): 
  self.capacity = capacity 
  self.size = 0
  self.table = [None] * capacity 

 def _hash(self, key): 
  return hash(key) % self.capacity 

 def insert(self, key, value): 
  index = self._hash(key) 

  if self.table[index] is None: 
   self.table[index] = Node(key, value) 
   self.size += 1
  else: 
   current = self.table[index] 
   while current: 
    if current.key == key: 
     current.value = value 
     return
    current = current.next
   new_node = Node(key, value) 
   new_node.next = self.table[index] 
   self.table[index] = new_node 
   self.size += 1

 def search(self, key): 
  index = self._hash(key) 

  current = self.table[index] 
  while current: 
   if current.key == key: 
    return current.value 
   current = current.next

  raise KeyError(key) 

 def __len__(self): 
  return self.size 
 
 def __str__(self):
  elements = []
  for i in range(self.capacity):
   current = self.table[i]
   while current:
    elements.append((current.key, current.value))
    current = current.next
  return str(elements)

 def __contains__(self, key): 
  try: 
   self.search(key) 
   return True
  except KeyError: 
   return False




########################################
 
ht = HashTable(5) 

 
ht.insert("apple", 3) 
ht.insert("banana", 2) 
ht.insert("cherry", 5) 

 
 
print('\n', len(ht), '\n') # 3

print('\n', ht, '\n')

assert len(ht) == 3, 'Error'

assert ht.search("banana") == 2
assert ht.search("apple") == 3
assert ht.search("cherry") == 5

