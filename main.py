def book_file():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            return file_contents.lower()
    except FileNotFoundError:
        print("File did not open. Check file")
    

def word_count(text):
    words = book_file()
    return len(words.split())

def letter_count(text):
    char_count = {}
    for char in text:            
        if char.isalpha():      
            char = char.lower()   
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count
    

    
    
def main():
    book = book_file()
    number_of_words = word_count(book)
    number_of_letters = letter_count(book)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document/n")

    for char in number_of_letters:
        print(f"The '{char}' character was found {number_of_letters[char]} times")


(main())