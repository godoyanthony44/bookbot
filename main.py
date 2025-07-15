import sys
from stats import *
def print_report(book_name,word_count,sorted_letters):
    with open("template.txt", "r") as f:
        template_contents = f.read()
    text_sorted = "\n"

    for letter in sorted_letters:
        text_sorted += "".join(f"{letter["letter"]}: {letter["count"]}")
        text_sorted += "\n"
    
    template_data = {
        'filename': book_name,
        'word_count':word_count,
        'data':text_sorted
    }
    return template_contents.format(**template_data)
    
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_input = sys.argv[1]
        print(book_input)
        book_contents = get_book_text(book_input)
        num_words = get_book_word_count(book_contents)
        num_letts = count_characters(book_contents)
        sorted_num_list = sorted_dict(num_letts)
        report = print_report(book_input, num_words,sorted_num_list)
        print(report)

main()
