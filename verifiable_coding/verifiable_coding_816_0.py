import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    M = int(data[0])
    books = list(map(int, data[1:M+1]))
    N = int(data[M+1])
    queries = list(map(int, data[M+2:M+2+N]))
    
    # Create a dictionary to map book numbers to their indices
    book_to_index = {book: i for i, book in enumerate(books)}
    
    # For each query, find the book at the given position
    # Since the books are being removed, we need to simulate the process
    # We'll use a list to represent the current state of the shelf
    shelf = books.copy()
    
    for query in queries:
        # Find the book at the given position (0-based or 1-based?)
        # The problem says "position from the left", which is 1-based
        # So we need to subtract 1
        pos = query - 1
        book = shelf[pos]
        print(book)
        # Remove the book from the shelf
        shelf.pop(pos)
    
if __name__ == '__main__':
    solve()