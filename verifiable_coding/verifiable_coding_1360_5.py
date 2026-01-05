import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        S1 = input[idx]
        idx += 1
        S2 = input[idx]
        idx += 1
        
        len1 = len(S1)
        len2 = len(S2)
        
        min_ugliness = float('inf')
        
        # Try all possible overlaps
        for i in range(len1):
            for j in range(len2):
                if S1[i] == S2[j]:
                    # Calculate petal lengths
                    l1 = i
                    l2 = j
                    l3 = len1 - i - 1
                    l4 = len2 - j - 1
                    # Calculate ugliness
                    ugliness = abs(l1 - l2) + abs(l2 - l3) + abs(l3 - l4) + abs(l4 - l1)
                    if ugliness < min_ugliness:
                        min_ugliness = ugliness
        
        print(min_ugliness)

if __name__ == '__main__':
    solve()