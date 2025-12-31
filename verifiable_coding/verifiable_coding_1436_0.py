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
        # The minimal number of military troops is the number of distinct characters in H
        # Because each troop can remove all occurrences of one character (either 'a' or 'b')
        # So, if there are both 'a' and 'b', we need 2 troops
        # If there is only one type, we need 1 troop
        if 'a' in H and 'b' in H:
            print(2)
        else:
            print(1)

if __name__ == '__main__':
    solve()