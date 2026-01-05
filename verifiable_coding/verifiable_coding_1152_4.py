import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    recipes = []
    for _ in range(N):
        if idx >= len(data):
            break
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        parts = line.split(b' ', 1)
        if len(parts) < 2:
            continue
        s = parts[0].decode('utf-8')
        v = int(parts[1].decode('utf-8'))
        recipes.append((s, v))
    
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        if idx >= len(data):
            break
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        queries.append(line.decode('utf-8'))
    
    # Build a trie for efficient prefix matching
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.max_priority = -float('inf')
            self.recipe = ""
    
    root = TrieNode()
    
    for s, v in recipes:
        node = root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if v > node.max_priority:
                node.max_priority = v
                node.recipe = s
    
    for q in queries:
        node = root
        found = False
        for c in q:
            if c not in node.children:
                break
            node = node.children[c]
            found = True
        if not found:
            print("NO")
        else:
            print(node.recipe)
    
if __name__ == '__main__':
    solve()