import sys
from stats import number_of_words_in_string
from stats import number_of_characters_in_string
from stats import sorted_list_of_dictionaries

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def main():
  if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_link = sys.argv[1]
  book_text = get_book_text(book_link)
  number_of_words_in_book = number_of_words_in_string(book_text)
  number_of_characters_in_book = number_of_characters_in_string(book_text)
  sorted_list_of_number_of_characters_in_book = sorted_list_of_dictionaries(number_of_characters_in_book)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_link}")
  print("----------- Word Count ----------")
  print(f"Found {number_of_words_in_book} total words")
  print("--------- Character Count -------")
  for list in sorted_list_of_number_of_characters_in_book:
    if(list["char"].isalpha()):
      print(f"{list["char"]}: {list["num"]}")

main()
