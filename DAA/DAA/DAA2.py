class Node:
    """A Huffman Tree Node"""

    def __init__(self, freq_, symbol_, left_=None, right_=None):
        # frequency of symbol
        self.freq = freq_
        # symbol name (character)
        self.symbol = symbol_
        # node left of the current node
        self.left = left_
        # node right of the current node
        self.right = right_
        # tree direction (0/1)
        self.huff = ""

def print_nodes(node, val=""):
    """Utility function to print Huffman codes for all symbols in the newly created Huffman tree"""
    # Huffman code for the current node
    new_val = val + str(node.huff)
    
    # If the node is not an edge node, then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    
    # If the node is an edge node, display its Huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

# Characters for the Huffman tree
chars = ["a", "b", "c", "d", "e", "f"]

# Frequency of characters
freq = [5, 9, 12, 13, 16, 45]

# List containing Huffman tree nodes of characters and frequencies
nodes = [Node(freq[x], chars[x]) for x in range(len(chars))]

while len(nodes) > 1:
    # Sort all the nodes in ascending order based on their frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
    
    # Pick the 2 smallest nodes
    left = nodes[0]
    right = nodes[1]
    
    # Assign directional values to these nodes
    left.huff = "0"
    right.huff = "1"
    
    # Combine the 2 smallest nodes to create a new node as their parent
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    
    # Remove the 2 nodes and add their parent as a new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print("Characters :", f'[{", ".join(chars)}]')
print("Frequency :", freq, "\n\nHuffman Encoding:")
print_nodes(nodes[0])
