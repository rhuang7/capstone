import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        rows = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            rows.append(row)
            idx += m
        
        cols = []
        for _ in range(m):
            col = list(map(int, data[idx:idx+n]))
            cols.append(col)
            idx += n
        
        row_set = set(tuple(row) for row in rows)
        col_set = set(tuple(col) for col in cols)
        
        # Find the correct row order
        row_order = []
        for row in rows:
            if tuple(row) in row_set and tuple(row) not in col_set:
                row_order.append(row)
        
        # Find the correct column order
        col_order = []
        for col in cols:
            if tuple(col) in col_set and tuple(col) not in row_set:
                col_order.append(col)
        
        # Create the table
        table = []
        for r in row_order:
            table_row = []
            for c in col_order:
                table_row.append(r[0])
                r = r[1:]
            table.append(table_row)
        
        # Output the table
        for row in table:
            results.append(' '.join(map(str, row)) + ' ')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()