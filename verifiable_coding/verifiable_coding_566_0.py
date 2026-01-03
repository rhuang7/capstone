import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        A = data[index]
        index += 1
        B = data[index]
        index += 1
        
        # Check if there is at least one common character between A and B
        # If there is, then we can choose s1 as that character and s2 as that character, making s1 + s2 a palindrome
        common = set(A) & set(B)
        if common:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()