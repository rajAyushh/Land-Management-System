import hashlib

class MerkleTreeNode:
def init(self,value):
self.left = None
self.right = None
self.hashValue = hashlib.sha256(bytes(value,'utf-8')).hexdigest()

def buildTree(leaves):
nodes = []
for i in leaves:
nodes.append(MerkleTreeNode(i))

while len(nodes)!=1:
    temp = []
    for i in range(0,len(nodes),2):
        node1 = nodes[i]
        if i+1 < len(nodes):
            node2 = nodes[i+1]
        else:
            temp.append(nodes[i])
            break
        concatenatedHash = node1.hashValue + node2.hashValue
        parent = MerkleTreeNode(concatenatedHash)
        parent.left = node1
        parent.right = node2
        temp.append(parent)
    nodes = temp 
return nodes[0].hashValue
