import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        voters = []
        for _ in range(n):
            m_i = int(data[idx])
            p_i = int(data[idx + 1])
            idx += 2
            voters.append((m_i, p_i))
        
        # Sort voters by m_i in descending order
        voters.sort(reverse=True, key=lambda x: x[0])
        
        # Use a union-find (disjoint set union) structure to track connected components
        parent = list(range(n))
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        # For each voter, try to add them to the component of their m_i voters
        # We'll keep track of the minimum cost to get a component of size s
        # We'll use a priority queue (heap) to select the cheapest way to get a component
        # We'll also use a dictionary to track the minimum cost for each size
        import heapq
        heap = []
        cost = {}
        
        for i in range(n):
            m_i, p_i = voters[i]
            # Find the root of the m_i voters
            root = find(m_i)
            # If the component of m_i voters has size s, we can add this voter to it
            # with cost p_i
            s = 1
            while True:
                if root in cost:
                    # We can add this voter to the component of size s
                    new_s = s + 1
                    new_cost = cost[root] + p_i
                    if new_s not in cost or new_cost < cost[new_s]:
                        cost[new_s] = new_cost
                    break
                else:
                    # We need to find the root of the component of size s
                    # which is the root of the m_i voters
                    # but we need to find the size of the component
                    # we can do this by finding the root of the m_i voters and then
                    # finding the size of the component
                    # but we need to track the size of each component
                    # so we need to track the size of each component
                    # we'll add a size array
                    size = [1] * n
                    def find_with_size(u):
                        while parent[u] != u:
                            parent[u] = parent[parent[u]]
                            u = parent[u]
                        return u
                    
                    root = find_with_size(m_i)
                    s = size[root]
                    # Now, we can add this voter to the component of size s
                    new_s = s + 1
                    new_cost = cost.get(root, 0) + p_i
                    if new_s not in cost or new_cost < cost[new_s]:
                        cost[new_s] = new_cost
                    break
        
        # The answer is the minimum cost to get a component of size n
        results.append(cost.get(n, 0))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()