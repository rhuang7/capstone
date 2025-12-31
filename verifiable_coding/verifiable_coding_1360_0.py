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
                    # Calculate the petal lengths
                    l1 = i + 1
                    l2 = len1 - i
                    l3 = j + 1
                    l4 = len2 - j
                    # Calculate ugliness
                    ugliness = abs(l1 - l2) + abs(l2 - l3) + abs(l3 - l4) + abs(l4 - l1)
                    min_ugliness = min(min_ugliness, ugliness)
        
        print(min_ugliness)

if __name__ == '__main__':
    solve()