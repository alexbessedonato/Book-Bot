from stats import get_num_words, get_num_characters, dictionary_to_list 
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dictionary = get_num_characters(text)
    list_of_dictionaries = dictionary_to_list(character_dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_of_dictionaries:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()