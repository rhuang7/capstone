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
        # Create a set of all elements
        all_elements = set()
        for row in rows:
            all_elements.update(row)
        # Create a dictionary to map values to their positions
        value_to_pos = {}
        for i in range(n):
            for j in range(m):
                value_to_pos[rows[i][j]] = (i, j)
        # Create a set of all elements in columns
        col_elements = set()
        for col in cols:
            col_elements.update(col)
        # Create a dictionary to map values to their column positions
        value_to_col = {}
        for i in range(m):
            for j in range(n):
                value_to_col[cols[i][j]] = i
        # Create the table
        table = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                # Find the value that is in the i-th row and j-th column
                # It must be the value that is in the i-th row of the rows list
                # and in the j-th column of the cols list
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of cols
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of cols
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of cols
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of cols
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of cols
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of cols
                # So we find the value that is in the i-th row of rows and in the j-th column of cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols
                # So we find the value that is in the i-th row of the rows and in the j-th column of the cols
                # This is the value that is in the i-th row of the rows and in the j-th column of the cols