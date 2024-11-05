import ssl
import certifi
import nltk

# Define a function to create the default HTTPS context
def create_default_https_context():
    return ssl.create_default_context(cafile=certifi.where())

# Use the function to set the default HTTPS context
ssl._create_default_https_context = create_default_https_context

nltk.download('words')

from nltk.corpus import words

# Load the dictionary of English words as a set for fast lookup
dictionary = set(words.words())

def get_matrix():
    print("Enter a 4x4 matrix of letters, row by row:")
    matrix = []
    for _ in range(4):
        row = input().strip().split()  # Read each row
        if len(row) != 4:
            raise ValueError("Each row must contain exactly 4 letters.")
        matrix.append(row)
    return matrix

def is_word(word):
    return len(word) > 3 and word in dictionary

def find_words(matrix):
    rows, cols = len(matrix), len(matrix[0])
    found_words = set()

    # All possible directions (up, down, left, right, and 4 diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def dfs(x, y, path, visited):
        # Add the current letter to the path and mark it visited
        word = ''.join(path)
        if len(word) > 1 and is_word(word):
            found_words.add(word)

        # Traverse all eight possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny, path + [matrix[nx][ny]], visited)
                visited.remove((nx, ny))  # Backtrack

    # Start DFS from every cell in the matrix
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, [matrix[i][j]], {(i, j)})

    return found_words

def main():
    matrix = get_matrix()
    words = find_words(matrix)
    print("Words found in the matrix:")
    for word in sorted(words):
        print(word)

if __name__ == "__main__":
    main()