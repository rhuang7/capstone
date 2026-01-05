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
        # Convert each number to its exponent (log2)
        # We'll use a dictionary to count occurrences of each exponent
        exp_count = {}
        for num in s:
            exp = num.bit_length() - 1
            if exp in exp_count:
                exp_count[exp] += 1
            else:
                exp_count[exp] = 1
        
        # Try to build up to 2048 (which is 2^11)
        # We need to have at least one 2048, or enough lower numbers to combine into it
        # Start from 11 and go down
        # We need to check if we can combine numbers to reach 11
        # For each exponent, we can combine pairs to go up
        # We'll track how many of each exponent we have
        # We'll start from 11 and go down to 0
        # If we can reach 11, then we can make 2048
        
        # We'll use a list to track the count of each exponent from 0 to 11
        # Since 2048 is 2^11, we need to check up to 11
        # We'll create a list of counts for exponents 0 to 11
        counts = [0] * 12
        for exp in exp_count:
            if exp <= 11:
                counts[exp] = exp_count[exp]
        
        # Now try to build up from the lowest exponents to the highest
        # We'll go from 0 to 11
        for i in range(11, -1, -1):
            # For each exponent, we can combine pairs to go up
            # We can combine pairs of i to make i+1
            # So we can carry over the number of pairs to i+1
            # The number of pairs is counts[i] // 2
            pairs = counts[i] // 2
            counts[i + 1] += pairs
            counts[i] %= 2
        
        if counts[11] >= 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()