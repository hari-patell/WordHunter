# WordHunter

WordHunter is a tool designed to help you find all possible words within a 4x4 grid of letters, mimicking the gameplay of popular word-hunting games. With this code, you can explore all possible word combinations that can be formed by connecting letters in a grid, following adjacency rules (diagonally or orthogonally).

## Features

- Accepts a 4x4 matrix of letters entered by the user.
- Finds all valid words by connecting letters in adjacent cells.
- Uses a dictionary of English words for validation to ensure only real words are returned.

## Setup Instructions

### Prerequisites

1. **Python 3** - Make sure you have Python 3 installed on your system.
2. **NLTK (Natural Language Toolkit)** - Used to access an English word list.

### Installation

1. Clone this repository (or copy the code) to your local machine.
2. Install Required Libraries:

   In order to run WordHunter, you need to install two libraries: `nltk` for the dictionary of words and `certifi` for SSL certificate handling on macOS.

   Open your terminal and run the following commands:

   ```
   python3 -m pip install nltk certifi
   ```

3. Download NLTK Word Corpus:

   This code requires the NLTK words corpus. To download it, open a Python shell or add this to your code temporarily:

   ```python
   import nltk
   nltk.download('words')
   ```

**Troubleshooting Installation**

On macOS, you may encounter SSL certificate errors when downloading NLTK data. If this happens, you can resolve it by configuring Python to use certifi's certificate bundle:

```python
import ssl
import certifi
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())
```

## Usage

1. Run the code by executing the script:

   ```
   python3 main.py
   ```

2. Enter the 4x4 Matrix:

   The program will prompt you to enter a 4x4 matrix of letters, row by row. For example:

   ```
   Enter a 4x4 matrix of letters, row by row:
   a b c d
   e f g h
   i j k l
   m n o p
   ```

3. Output:

   The program will display all valid words found within the matrix, sorted alphabetically.

Example:

Input:
```
Enter a 4x4 matrix of letters, row by row:
c a t s
r a t e
t a p e
s o n g
```

Output:
```
Words found in the matrix:
cat
cats
rat
rate
tape
song
```

## License

This project is for educational purposes only. Using it in competitive games or challenges may be against the rules of such games. Use responsibly! 😈
