import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    L = int(data[1])
    strings = data[2:2+N]
    
    # Sort the strings using custom comparator
    # Compare two strings a and b by checking a + b vs b + a
    strings.sort(key=lambda x: x)
    
    # Concatenate the sorted strings
    result = ''.join(strings)
    print(result)

if __name__ == '__main__':
    solve()