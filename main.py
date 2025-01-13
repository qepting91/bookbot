def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1
    return chars

def sort_on(dict):
    return dict["count"]

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{get_word_count(file_contents)} words found in the document\n")
        
        # Get character counts and convert to sortable list
        char_counts = get_char_count(file_contents)
        chars_list = [{"char": char, "count": count} for char, count in char_counts.items()]
        chars_list.sort(reverse=True, key=sort_on)
        
        # Print each character count
        for char_dict in chars_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
            
        print("--- End report ---")

main()