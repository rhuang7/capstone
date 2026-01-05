import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        # For a puzzle to be solvable, it must be possible to arrange the pieces such that
        # every adjacent pair fits. This is only possible if at least one of n or m is 1.
        # Because if both are greater than 1, then the puzzle cannot be arranged in a way
        # that satisfies the conditions (as shown in the note for the second test case).
        if n == 1 or m == 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()