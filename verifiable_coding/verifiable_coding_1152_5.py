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
        line = data[idx].split(b' ')
        if len(line) < 2:
            idx += 1
            continue
        S = line[0]
        V = int(line[1])
        recipes.append((S, V))
        idx += 1
    
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        if idx >= len(data):
            break
        queries.append(data[idx])
        idx += 1
    
    # Build a trie for efficient prefix matching
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.max_priority = -float('inf')
            self.recipe = None
    
    root = TrieNode()
    
    for S, V in recipes:
        node = root
        for c in S:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if V > node.max_priority:
                node.max_priority = V
                node.recipe = S
        # After processing the entire recipe, update the max priority
        if V > node.max_priority:
            node.max_priority = V
            node.recipe = S
    
    for query in queries:
        node = root
        found = False
        for c in query:
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