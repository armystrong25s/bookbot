def char_count(text):
    text = text.lower()
    counts = {}

    for char in text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    return counts

def word_count(text):
    words = text.split()
    return len(words)

def generate_report(file_name, word_count_result, char_count_result):
    print(f"--- Begin reportof {file_name} ---")
    print(f"{word_count_result} words was found in the document\n")

    for char, count in sorted(char_count_result.items()):
        print(f"The '{char}' character was found {count} times")

    print(f"--- End report ---")


def main():
    # Your file reading code goes here
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()
        
    # Call word_count and print the result
    word_count_result = word_count(file_contents)
    

    # Call char_count and print the result
    char_count_result = char_count(file_contents)
    
    generate_report(file_name, word_count_result, char_count_result)

# Don't forget to call main()
if __name__ == "__main__":
    main()
