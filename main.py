def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    char_dict = get_letter_count(text)
    char_list = create_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)

    for char in char_list:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {str(char[1]).ljust(5, ' ')} times")

    print("--- End report ---")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    char_dict = {}
    words = text.split()
    all_words = "".join(words).lower()
    for char in all_words:
        if char in char_dict:
           char_dict[char] += 1
        else:
           char_dict[char] = 1
    return char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict[1]

def create_list(dict):
    return list(dict.items())

main()
