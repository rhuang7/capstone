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
        if not line:
            idx += 1
            continue
        parts = line.split(b' ', 1)
        if len(parts) < 2:
            idx += 1
            continue
        s = parts[0].decode()
        v = int(parts[1].decode())
        recipes.append((s, v))
        idx += 1
    
    Q = int(data[idx].decode()) if idx < len(data) else 0
    idx += 1
    
    queries = []
    for _ in range(Q):
        if idx >= len(data):
            break
        line = data[idx].strip()
        if line:
            queries.append(line.decode())
        idx += 1
    
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
    
    for query in queries:
        node = root
        found = False
        for c in query:
            if c not in node.children:
                break
            node = node.children[c]
            found = True
        if found and node.max_priority != -float('inf'):
            print(node.recipe)
        else:
            print("NO")

if __name__ == '__main__':
    solve()