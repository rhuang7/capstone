import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    H_list = data[1:T+1]
    
    for H in H_list:
        if len(H) == 0:
            print(0)
            continue
        # The minimal number of military troops is 1 if the string is not empty
        # Because we can always delete the entire string as a palindromic subsequence
        print(1)

if __name__ == '__main__':
    solve()