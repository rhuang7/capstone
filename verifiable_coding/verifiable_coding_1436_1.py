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
        # The minimal number of troops is 1 if the string is not empty
        # because we can always delete the entire string as a palindromic subsequence
        # However, if the string is made of only 'a's or only 'b's, we can delete it in 1 move
        # Otherwise, we need 2 moves: delete all 'a's in one move and all 'b's in another
        if 'a' not in H or 'b' not in H:
            print(1)
        else:
            print(2)
            
if __name__ == '__main__':
    solve()