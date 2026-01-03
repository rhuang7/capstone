import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    recipes = []
    for _ in range(N):
        s = data[idx]
        v = int(data[idx + 1])
        recipes.append((s, v))
        idx += 2
    
    Q = int(data[idx])
    idx += 1
    
    queries = data[idx:idx+Q]
    
    # Build a trie for the recipes
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.max_priority = -float('inf')
            self.recipe = None
    
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
        # After processing the entire string, update the max priority
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