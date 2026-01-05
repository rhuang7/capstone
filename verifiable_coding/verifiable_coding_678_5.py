import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        people = [0] * N
        people[0] = 1
        day = 0
        
        while sum(people) < N:
            day += 1
            new_people = 0
            for i in range(N):
                if people[i] > 0:
                    if i + 1 < N and people[i + 1] == 0:
                        people[i + 1] = 1
                        new_people += 1
                        if new_people == A[i]:
                            break
            if new_people == 0:
                break
        
        results.append(str(day))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()