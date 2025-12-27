def check(candidate):
    assert candidate(12,[2,7,13,19])==32
    assert candidate(10,[2,7,13,19])==26
    assert candidate(100,[2,7,13,19])==5408


import heapq

def find_nth_super_ugly_number(primes, n):
    # Initialize the heap with the first super ugly number (1)
    heap = [1]
    # Use a set to keep track of numbers we've already added to the heap
    seen = {1}
    
    # Initialize the result list
    result = []
    
    # Extract the nth super ugly number
    for _ in range(n):
        # Pop the smallest element from the heap
        current = heapq.heappop(heap)
        result.append(current)
        
        # Generate new numbers by multiplying the current number with each prime
        for prime in primes:
            next_num = current * prime
            if next_num not in seen:
                seen.add(next_num)
                heapq.heappush(heap, next_num)
    
    return result[-1]

check(find_nth_super_ugly_number)