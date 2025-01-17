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

def sort(s):
    return s["count"]

def sorted_list(text):
    list_items = []
    for char, count in text.items():
        list_items.append({"char":char, "count":count})
    list_items.sort(reverse=True, key=sort)
    return list_items
    
def main():
    book = book_file()
    num_of_words = word_count(book)
    number_of_letters = letter_count(book)
    sorted_char_list = sorted_list(number_of_letters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")

    for letter in sorted_char_list:
        print(f"The '{letter["char"]}' character was found {letter["count"]}")  
main()