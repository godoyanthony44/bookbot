def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_book_word_count(contents):
    contents = contents.split()
    return len(contents)

def count_characters(contents):
    contents_count = {}
    for letter in contents:
        letter = letter.lower()
        if letter not in contents_count:
            contents_count[letter] = 1
        else:
            contents_count[letter] +=1
    return contents_count

def sort_on(contents):
    return contents["count"]

def sorted_dict(contents):
    sort_list = []
    for letter in contents:
        if letter.isalpha():
            sort_list.append({"letter":letter,"count":contents[letter]})
    sort_list.sort(reverse=True,key=sort_on)
    return sort_list
