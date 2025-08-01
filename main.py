import sys




def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)

from stats import count_words, is_an_alpha, count_letters, split_dict, sort_letters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path_to_file = sys.argv[1]
    print("Analyzing book found at", path_to_file)
    book_text = get_book_text(path_to_file)
    lettercount_us = count_letters(book_text)
    lettercount_us = is_an_alpha(lettercount_us)
    print("----------- Word Count ----------")
    print("Found", count_words(book_text), "total words")
    print("--------- Character Count -------")
    lettercount_d = split_dict(lettercount_us)
    lettercount_d.sort(reverse=True, key=sort_letters)
    for d in lettercount_d:
        pl = [":"]
        for key, value in d.items():
            if key == "char":
                pl.insert(0, value)
            elif key == "num":
                pl.append(value)
        pl[0] = pl[0] + pl[1]
        del pl[1]
        
        print(pl[0], pl[1],)
    print("============= END ===============")

main()
