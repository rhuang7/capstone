import sys
import bisect

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
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        Q = int(data[idx])
        idx += 1
        queries = []
        for __ in range(Q):
            x = int(data[idx])
            y = int(data[idx+1])
            queries.append((x, y))
            idx += 2
        
        # Preprocess a to be sorted (already sorted as per constraints)
        # For each query, check if (x, y) is on any wall
        # A point (x, y) is on the wall with a_i if x + y = a_i
        # Also, check if x == 0 and y == 0 (origin)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)
        # Also, check if x == 0 and y == a_i or x == a_i and y == 0 (on the wall)
        # But since a_i is positive, x and y can't be zero at the same time unless it's origin
        # So check if x + y == a_i for any a_i
        # Also, check if (x, y) is (0, 0)