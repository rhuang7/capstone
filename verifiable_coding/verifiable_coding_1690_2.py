import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    
    people = []
    president_id = set()
    for _ in range(N):
        p = int(data[idx])
        idx += 1
        id = set(map(int, data[idx:idx+p]))
        idx += p
        people.append(id)
        if _ == 0:
            president_id = id
    
    # Build a map from element to list of people (indices)
    element_to_people = defaultdict(list)
    for i, id in enumerate(people):
        for elem in id:
            element_to_people[elem].append(i)
    
    # BFS to find all people in the extended family
    visited = set()
    queue = deque()
    queue.append(0)
    visited.add(0)
    
    while queue:
        person = queue.popleft()
        for elem in people[person]:
            for neighbor in element_to_people[elem]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    print(len(visited))

if __name__ == '__main__':
    solve()