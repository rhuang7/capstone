import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        S1 = data[index]
        S2 = data[index+1]
        index += 2
        
        len1 = len(S1)
        len2 = len(S2)
        
        min_ugliness = float('inf')
        
        # Find all possible overlapping positions
        for i in range(len1):
            for j in range(len2):
                if S1[i] == S2[j]:
                    # Overlap at position i in S1 and j in S2
                    # Calculate petal lengths
                    # S1 part: from i to end
                    # S2 part: from j to end
                    # The overlapping character is counted once
                    # So petal lengths are:
                    # len1 - i (from S1)
                    # len2 - j (from S2)
                    # But since they overlap at one character, the total is:
                    # (len1 - i) + (len2 - j) - 1 (overlap)
                    # But we need to split into two parts, so we can choose any split
                    # The minimum ugliness is when the two parts are as equal as possible
                    # So we can try all possible splits of the combined length
                    total = (len1 - i) + (len2 - j) - 1
                    if total == 0:
                        # All petals are 0, ugliness is 0
                        min_ugliness = 0
                        break
                    # Try all possible splits of the total length into two parts
                    for k in range(1, total):
                        l1 = k
                        l2 = total - k
                        # Ugliness is |l1 - l2| + |l2 - l1| + |l1 - l2| + |l2 - l1|
                        # Which simplifies to 2 * (|l1 - l2| + |l2 - l1|) = 4 * |l1 - l2|
                        ugliness = 4 * abs(l1 - l2)
                        if ugliness < min_ugliness:
                            min_ugliness = ugliness
                    if min_ugliness == 0:
                        break
            if min_ugliness == 0:
                break
        
        print(min_ugliness)

if __name__ == '__main__':
    solve()