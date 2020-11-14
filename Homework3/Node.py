class Node:
  def __init__(self, node_id):
    self.id = node_id
    self.children = []
  
  def add_child(self, new_child):
    self.children.append(new_child)
 
    
def save_edges(root):
  traversal = []
  traversal.append(root.id)
  
  def preorder_traversal(node):
    for node in node.children:
      traversal.append(node.id)
      preorder_traversal(node)
      
  preorder_traversal(root)
  return traversal
  

def save_Newick(ids, root):
  traversal = []
  
  def postorder_traversal(node):
    for node in node.children:
      postorder_traversal(node)
      traversal.append(node.id)
      
  postorder_traversal(root)
  return traversal
  
  
child9 = Node("child9")
child10 = Node("child10")
child11 = Node("child11")

child6 = Node("child6")
child6.add_child(child9)
child6.add_child(child10)
child6.add_child(child11)
child7 = Node("child7")
child8 = Node("child8")

child2 = Node("child2")
child2.add_child(child6)
child2.add_child(child7)
child2.add_child(child8)

child3 = Node("child3")
child4 = Node("child4")
child5 = Node("child5")

child1 = Node("child1")
child1.add_child(child3)
child1.add_child(child4)
child1.add_child(child5)


root = Node("root")
root.add_child(child1)
root.add_child(child2)

# print(save_edges(root))
# print(save_Newick(1, root))


def generate_fake_matrix():
  length = 6
  distance_matrix = []
    # sets all distance_matrix values to None/null
  for i in range(0, length):
    row = []
    for j in range(0, length):
      row.append(None)
    distance_matrix.append(row)
  distance_matrix[0][0] = ""
    
  ids = ["a", "b", "c", "d", "e"]
  # First row indicators
  for i in range(1, length):
    distance_matrix[0][i] = ids[i-1]

  # First column indicator
  for j in range(1, length):
    distance_matrix[j][0] = ids[j-1]
  
  lst = [[0,5,9,9,8],
   [5,0,10,10,9],
   [9,10,0,8,7],
   [9,10,8,0,3,],
   [8,9,7,3,0]
   ]

  # # Calculate the distance_matrix
  for i in range(1, length):
    for j in range(1, length):
      distance_matrix[i][j] = lst[i-1][j-1]
      
  # for i in range(0, length):
  #   row = []
  #   for j in range(0, length):
  #     row.append(distance_matrix[i][j])
  #   print(row)
  return distance_matrix