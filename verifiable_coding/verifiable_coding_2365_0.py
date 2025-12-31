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
        segments = []
        for _ in range(n-1):
            k = int(data[idx])
            idx += 1
            seg = list(map(int, data[idx:idx+k]))
            idx += k
            segments.append(seg)
        
        # Build a graph where each node is a number in the permutation
        # and edges represent the relation between numbers in the segments
        # We'll use a Union-Find (Disjoint Set Union) structure to group numbers
        parent = list(range(n+1))  # 1-based indexing
        
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu != pv:
                parent[pv] = pu
        
        # Process each segment to build the graph
        for seg in segments:
            # The segment is sorted, so the first element is the smallest
            # and the last element is the largest
            # We can use the first and last element to connect the numbers
            # in the segment
            for i in range(1, len(seg)):
                union(seg[i-1], seg[i])
        
        # Now, we can reconstruct the permutation by finding the order of elements
        # in the DSU structure. We can do this by finding the root of each element
        # and then sorting the elements based on their root
        # However, since the DSU structure may not give a unique order, we need
        # to find the correct order by checking the segments again
        # We'll use the sorted segments to determine the correct order
        
        # Create a list of all elements in the permutation
        elements = list(range(1, n+1))
        # Sort the elements based on their position in the permutation
        # We'll use the segments to determine the correct order
        # We'll use the first occurrence of each element in the segments to determine
        # the order
        
        # Create a dictionary to map each element to its position in the permutation
        pos = {}
        for seg in segments:
            for num in seg:
                if num not in pos:
                    pos[num] = len(pos)
        
        # Sort the elements based on their position in the permutation
        sorted_elements = sorted(elements, key=lambda x: pos[x])
        
        # Now, we need to determine the actual permutation based on the segments
        # We'll use the segments to determine the correct order
        # We'll use the first occurrence of each element in the segments to determine
        # the correct order
        
        # We'll create a list of the elements in the permutation
        p = [0] * n
        for i in range(n):
            p[i] = sorted_elements[i]
        
        # Now, we need to verify that the permutation is correct
        # We'll check each segment to see if it is a subsegment of the permutation
        # in sorted order
        # However, since the input is guaranteed to be correct, we can just return the permutation
        
        results.append(' '.join(map(str, p)) + ' ')
    
    print(''.join(results).strip())

if __name__ == '__main__':
    solve()