def number_of_words_in_string(string):
  string_list = string.split()
  number_of_words = len(string_list)
  return number_of_words

def number_of_characters_in_string(string):
  char_list = list(string)
  lowercase_char_list = []
  for char in char_list:
    lowercase_char_list.append(char.lower())
  chars_dict = {}
  for char in lowercase_char_list:
    if (char in chars_dict):
      chars_dict[char] += 1
    else:
      chars_dict[char] = 1
  return(chars_dict)

def sorted_list_of_dictionaries(dict_of_chars):
  list_of_dictionaries = []
  for entry in dict_of_chars:
    list_of_dictionaries.append({"char": entry, "num": dict_of_chars[entry]})
  def sort_by_num(dict):
    return dict['num']
  list_of_dictionaries.sort(reverse=True, key=sort_by_num)
  return list_of_dictionaries

