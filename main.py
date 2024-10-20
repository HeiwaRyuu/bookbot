import os

def sort_on(dict):
    return dict["num"]

def character_occ_count(text):
    lc_text = text.lower()
    char_count = {}
    for char in lc_text:
        if char not in char_count.keys():
            char_count[char] = 0
        char_count[char] += 1
     
    return char_count

def count_words(text):
    lst_of_words = text.split()
    return len(lst_of_words)

def print_report(data, frankenstein_book_path):
    print(f"--- Begin report of {frankenstein_book_path} ---")
    words = count_words(data) 
    print(f"{words} found in the document")
    char_count = character_occ_count(data)
    
    dict_lst = []
    for key, value in char_count.items():
        dict_lst.append({"char":key, "num":value})
    ## Sorting by largest to lowest occurencies
    dict_lst.sort(reverse=True, key=sort_on)

    for dict in dict_lst:
        if dict["char"].isalpha():
            key = dict["char"]
            value = dict["num"]
            print(f"The \'{key}\' character was found {value} times")
    print("--- End report ---")

def main():
    cwd = os.getcwd()
    books_path = cwd + r"/books"
    frankenstein_book_path = books_path + "/frankenstein.txt"
    with open(frankenstein_book_path, "r") as f:
        data = f.read()
    print_report(data, frankenstein_book_path)

if __name__ == "__main__":
    main()
