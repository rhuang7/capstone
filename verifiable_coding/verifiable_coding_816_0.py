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
    
    # Create a list to represent the current positions of the books
    current_positions = list(range(M))
    
    # Process each query
    for i in range(N):
        pos = queries[i]
        # Find the book at the given position
        book = books[current_positions[pos-1]]
        # Remove the book from the current_positions list
        current_positions.pop(pos-1)
        # Output the book
        print(book)
        
if __name__ == '__main__':
    solve()