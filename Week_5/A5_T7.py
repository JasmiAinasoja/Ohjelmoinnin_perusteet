DELIMITER = ','

def collectWords():
    all_words = ""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        if all_words == "":
            all_words = word
        else:
            all_words = all_words + DELIMITER + word
    return all_words

def analyseWords(words_string):
    words = words_string.split(DELIMITER)
    word_count = len(words)
    char_count = 0
    for word in words:
        char_count = char_count + len(word)
    average = char_count / word_count
    print("-", word_count, "Words")
    print("-", char_count, "Characters")
    print("- {:.2f} Average word length".format(average))

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

main()