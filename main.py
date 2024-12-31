def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
def count_words():
    count = 0
    with open("books/frankenstein.txt") as f:
        words_arr = f.read().split()
    for word in words_arr:
        count += 1
    print(count)

    
count_words()

main()