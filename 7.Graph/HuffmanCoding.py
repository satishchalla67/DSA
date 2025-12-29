
import heapq
import itertools

class Node:
    def __init__(self, val, symbol=None):
        self.left = None
        self.right = None
        self.val = val
        self.symbol = symbol
        

    def is_leaf(self):
        return self.symbol is not None




def buildHuffmanTree(symbols_with_frequency):
    
    heap=[]
    counter = itertools.count()
    
    
    for sym, frq in symbols_with_frequency:
        node = Node(frq, symbol=sym)
        heapq.heappush(heap, (frq, next(counter), node))
        
        
    while len(heap)>1:
        f1, _, node1 = heapq.heappop(heap)
        f2, _, node2 = heapq.heappop(heap)
        
        node3 = Node(f1+f2)
        node3.left = node1
        node3.right = node2
        heapq.heappush(heap, (node3.val, next(counter), node3))
    return heap[0][2]


def build_codes(root):
    
    codes = {}
    
    def dfs(root, prefix):
        if not root:
            return None
        if root.is_leaf():
            codes[root.symbol] = prefix or "0"
        dfs(root.left, prefix+"0")
        dfs(root.right, prefix+ "1")
    dfs(root, "")
    return codes
            
        

def encode(chars, codes):
    return "".join([codes[char] for char in chars])


def decode(bits, root):
    node = root
    char=[]
    for bit in bits:
        node = node.left if bit=="0" else node.right
        if node.is_leaf():
            char.append(node.symbol)
            node=root
    return "".join(char)           


data = [("a", 45),
        ("b", 15),
        ("c", 2),
        ("d", 30),
        ("e", 5),
        ("f", 3)]

root = buildHuffmanTree(data)
codes = build_codes(root)

# for symbol, freq in sorted(codes.items(), key=lambda x : (len(x[1]), x[0])):
#     print(f'{symbol}: {freq}')
    
sample = "aefcd"
encoded = encode(sample, codes)
print(encoded)
decoded = decode(encoded, root)
print(decoded)