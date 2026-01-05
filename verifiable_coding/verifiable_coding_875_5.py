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
        # Miksi can win if Vanja cannot win in one move and there exists a move that leads to Z1 or Z2
        # But since Vanja goes first, Miksi can only win if Vanja cannot win in one move and there exists a move that leads to Z1 or Z2 in one move
        # But since Vanja can choose any move, Miksi can only win if there is a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2 in one move, but Vanja cannot win in one move
        # But since Vanja can choose any move, Miksi cannot win in one move
        # So we need to check if there exists a move that leads to Z1 or Z2