def open_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents.lower()

def count_words(book): #boots, quick question in a question. Should I replace the parameter with book_content?
    return len(book.split())


def count_characters(words):
    char_count = {}
    for char in words:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def main():
    inside_book = open_book()
    number_of_words = count_words(inside_book)
    character_count = count_characters(inside_book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print("\nCharacter counts: ")
    print(character_count)
if __name__ == "__main__":
    main() 