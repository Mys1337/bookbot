from stats import get_book_text
from stats import count
from stats import sorting
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    words = get_book_text(sys.argv[1])
    letters = count(words)
    sorted = sorting(letters)
    for item in sorted:
        print(f"{item['letter']}: {item['count']}")

main()