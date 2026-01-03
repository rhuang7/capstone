import sys
import math
from collections import deque

def get_distinct_three_digit_numbers_from_number(number):
    digits = list(str(number))
    unique_digits = set(digits)
    if len(unique_digits) < 3:
        return 0
    result = set()
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if k == i or k == j:
                    continue
                num = int(digits[i] + digits[j] + digits[k])
                result.add(num)
    return len(result)

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        K = int(input[idx])
        N = int(input[idx+1])
        idx += 2
        
        # Initial number
        current = K
        visited = set()
        visited.add(current)
        queue = deque([current])
        count = 0
        
        for _ in range(N):
            next_queue = deque()
            while queue:
                num = queue.popleft()
                distinct_numbers = get_distinct_three_digit_numbers_from_number(num)
                count += distinct_numbers
                for n in range(1000, 10000):
                    if n not in visited:
                        next_queue.append(n)
            queue = next_queue
        
        print(count)

if __name__ == '__main__':
    solve()