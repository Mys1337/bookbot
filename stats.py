def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = 0
        words = file_contents.split()
        for word in words:
            num_words += 1
        print(f"Found {num_words} total words")
    return words

def count(words):
    letters = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            letters[letter] = letters.get(letter, 0) + 1
    return letters

def sort_on(item):
    return item["count"]


def sorting(letters_dict):
    letters_list = [{"letter": k, "count": v} for k, v in letters_dict.items()]
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list