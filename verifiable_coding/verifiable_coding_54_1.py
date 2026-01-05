import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    
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
        # We'll use the exponent of 2 to represent the value
        # For example, 2^10 = 1024, 2^11 = 2048
        power_count = {}
        for num in count:
            exp = num.bit_length() - 1
            if exp in power_count:
                power_count[exp] += count[num]
            else:
                power_count[exp] = count[num]
        
        # Start from 10 (2^10 = 1024) and go up to 11 (2^11 = 2048)
        # We need at least 2 of 11 to make 2048
        # Or 1 of 11 and 1 of 10 (combine them to make 2048)
        # Or 2 of 10 and 1 of 9 (combine 2 of 10 to make 11, then combine with 9)
        # And so on...
        
        # We'll simulate the process of combining pairs
        # We'll start from the lowest exponent and work up
        # We'll track how many of each exponent we have
        # We'll try to combine pairs to get higher exponents
        
        # We'll use a list to represent the count of each exponent
        # From 0 to 20 (since 2^20 is 1,048,576 which is larger than 2048)
        exponents = [0] * 21
        for num in s:
            exp = num.bit_length() - 1
            exponents[exp] += 1
        
        # Try to combine pairs to get higher exponents
        # We'll process from the lowest exponent to the highest
        for i in range(20):
            # Combine as many pairs as possible
            pairs = exponents[i] // 2
            exponents[i] %= 2
            exponents[i + 1] += pairs
        
        if exponents[11] >= 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()