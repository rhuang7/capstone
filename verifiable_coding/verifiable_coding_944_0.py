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
        
        from collections import defaultdict
        pos = defaultdict(list)
        for i, num in enumerate(A):
            pos[num].append(i)
        
        max_sum = 0
        for num in pos:
            if len(pos[num]) < 2:
                continue
            positions = pos[num]
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    left = positions[i]
                    right = positions[j]
                    if left + 1 >= right - 1:
                        continue
                    subarray = A[left + 1:right]
                    total = sum(subarray)
                    if total == 0:
                        continue
                    count_even = 0
                    count_odd = 0
                    for num in subarray:
                        if num % 2 == 0:
                            count_even += 1
                        else:
                            count_odd += 1
                    if (count_even % 2 == 0 and count_odd % 2 == 1) or (count_even % 2 == 1 and count_odd % 2 == 0):
                        max_sum = max(max_sum, total)
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()