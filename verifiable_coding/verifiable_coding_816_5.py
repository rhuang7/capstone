import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    M = int(data[0])
    books = list(map(int, data[1:M+1]))
    N = int(data[M+1])
    queries = list(map(int, data[M+2:M+2+N]))
    
    # Create a dictionary to map book numbers to their current positions
    book_pos = {book: i for i, book in enumerate(books)}
    
    # For each query, find the book at the given position
    # Then remove it from the list and update the positions
    # Since N is small (<= 4000), we can afford O(N*M) time
    for i in range(N):
        pos = queries[i] - 1  # Convert to 0-based index
        book = books[pos]
        print(book)
        # Remove the book from the list
        books.pop(pos)
        # Update the positions of the remaining books
        for j in range(pos, len(books)):
            book_pos[books[j]] = j

if __name__ == '__main__':
    solve()