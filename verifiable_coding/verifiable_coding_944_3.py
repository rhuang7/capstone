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
        
        for key in pos:
            indices = pos[key]
            if len(indices) < 2:
                continue
            for i in range(len(indices) - 1):
                left = indices[i]
                right = indices[i + 1]
                if left + 1 >= right - 1:
                    continue
                subarray = A[left + 1:right]
                total = sum(subarray)
                even_count = 0
                odd_count = 0
                for num in subarray:
                    if num % 2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1
                if (even_count % 2 == 0 and even_count != 0 and odd_count == 0) or (odd_count % 2 == 1 and odd_count != 0 and even_count == 0):
                    if total > max_sum:
                        max_sum = total
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()