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
        id = set(map(int, data[idx:idx + p]))
        idx += p
        people.append(id)
        if _ == 0:
            president_id = id
    
    # Build a map from element to list of people (indices)
    element_to_people = defaultdict(list)
    for i, id in enumerate(people):
        for num in id:
            element_to_people[num].append(i)
    
    # BFS to find all people in the extended family
    visited = [False] * N
    queue = deque()
    queue.append(0)
    visited[0] = True
    count = 0
    
    while queue:
        current = queue.popleft()
        count += 1
        for num in people[current]:
            for neighbor in element_to_people[num]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    print(count)

if __name__ == '__main__':
    solve()