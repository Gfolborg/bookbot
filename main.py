def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
        
book = main()

def count_words(book):
    return len(book.split())

def count_characters(words):
    char_count = {}

    for char in words:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
            
    print(char_count)
         
words = book.lower()
count_characters(words)