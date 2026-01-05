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
        
        # Try all possible overlaps
        for i in range(len1):
            for j in range(len2):
                if S1[i] == S2[j]:
                    # Overlap at position i in S1 and j in S2
                    # The petals are formed by the parts of the strings on either side of the overlap
                    # Calculate the lengths of the petals
                    petal1 = i
                    petal2 = j
                    petal3 = len1 - i - 1
                    petal4 = len2 - j - 1
                    
                    # Calculate ugliness
                    ugliness = abs(petal1 - petal2) + abs(petal2 - petal3) + abs(petal3 - petal4) + abs(petal4 - petal1)
                    if ugliness < min_ugliness:
                        min_ugliness = ugliness
        
        print(min_ugliness)

if __name__ == '__main__':
    solve()