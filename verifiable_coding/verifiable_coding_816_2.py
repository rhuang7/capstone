import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    M = int(data[0])
    books = list(map(int, data[1:M+1]))
    N = int(data[M+1])
    queries = list(map(int, data[M+2:]))
    
    # Create a dictionary to map book numbers to their current positions
    book_pos = {book: i for i, book in enumerate(books)}
    
    # For each query, find the book at the given position
    # Then remove it from the list and update the positions
    # Since N is small (up to 4000), even O(N^2) is acceptable
    for i in range(N):
        pos = queries[i]
        # Find the book at the given position
        book = books[pos - 1]
        # Remove the book from the list
        books.pop(pos - 1)
        # Update the positions of the remaining books
        for j in range(pos, len(books)):
            books[j] -= 1
        # Output the book
        print(book)
        
if __name__ == '__main__':
    solve()