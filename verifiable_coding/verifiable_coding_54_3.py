import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    q = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(q):
        n = int(data[index])
        index += 1
        s = list(map(int, data[index:index + n]))
        index += n
        
        count = {}
        for num in s:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Count how many of each power of two we have
        # Convert each number to its exponent (log2)
        # For example, 2^10 is 1024, 2^11 is 2048
        # We need to reach 2^11 (2048)
        exponents = {}
        for num in s:
            exp = 0
            while num > 1:
                num >>= 1
                exp += 1
            exponents[exp] = exponents.get(exp, 0) + 1
        
        # Try to build up to 2048 (exp 11)
        # We need at least one way to combine numbers to reach 2048
        # We can use a greedy approach from the top down
        # Start from 11 and go down
        for exp in range(11, 0, -1):
            if exp in exponents:
                # We can use this to build up
                # We need to see if we can combine numbers to reach 2048
                # We need at least one occurrence of exp 11
                # If we have any occurrence of exp 11, we can just return YES
                if exp == 11:
                    results.append("YES")
                    break
                else:
                    # Try to combine pairs of lower exponents
                    # We need to see if we can combine exponents to reach higher ones
                    # We can use a greedy approach to see if we can reach 2048
                    # We can use a frequency array
                    freq = [0] * 12
                    for exp2 in exponents:
                        freq[exp2] = exponents[exp2]
                    
                    # Try to build up from lower exponents
                    for i in range(1, 12):
                        if freq[i] > 0:
                            # Combine pairs of i to make i+1
                            pairs = freq[i] // 2
                            freq[i+1] += pairs
                            freq[i] -= pairs * 2
                    # Check if we have at least one 11
                    if freq[11] >= 1:
                        results.append("YES")
                        break
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()