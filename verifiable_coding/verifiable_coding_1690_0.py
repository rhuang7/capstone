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
        id_set = set(map(int, data[idx:idx + p]))
        idx += p
        people.append(id_set)
        if _ == 0:
            president_id = id_set
    
    # Create a map from each element to the set of people it appears in
    element_to_people = defaultdict(list)
    for i, pid in enumerate(people):
        for elem in pid:
            element_to_people[elem].append(i)
    
    # BFS to find all people in the extended family
    visited = set()
    queue = deque()
    queue.append(0)
    visited.add(0)
    
    while queue:
        person = queue.popleft()
        for elem in people[person]:
            for other in element_to_people[elem]:
                if other not in visited:
                    visited.add(other)
                    queue.append(other)
    
    print(len(visited))

if __name__ == '__main__':
    solve()