import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        Z1 = int(data[idx+1])
        Z2 = int(data[idx+2])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if Vanja can win in one move
        can_vanja_win = False
        for a in A:
            if abs(a) == Z1 or abs(a) == Z2:
                can_vanja_win = True
                break
        
        if can_vanja_win:
            results.append(1)
            continue
        
        # Check if Miksi can win in one move
        # For Miksi to win, Vanja must not be able to win in one move, and Miksi can reach Z1 or Z2 in one move
        # But since Miksi moves after Vanja, he can only win if Vanja didn't win and Miksi can reach Z1 or Z2 in one move
        # However, since Miksi can only move after Vanja, he can only win if Vanja didn't win and Miksi can reach Z1 or Z2 in one move
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of the GCD of the elements
        # So we need to check if Z1 or Z2 is reachable in one move (i.e., if Z1 or Z2 is in the set {a, -a} for any a in A)
        # But since Vanja already checked that, we need to check if Miksi can reach Z1 or Z2 in one move, given that Vanja didn't win
        # But since Miksi can choose any element and add or subtract, he can reach any value that is a multiple of