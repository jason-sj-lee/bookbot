def count_words(str):
  words = str.split()
  return len(words)

def count_chars(str):
  char_count = {}
  lowered_string = str.lower()
  for c in lowered_string:
      if c in char_count:
        char_count[c] += 1
      else:
         char_count[c] = 1
  return char_count

def sort_on(dict):
    return dict["num"]

def gen_report(book_text):
  words = count_words(book_text)
  chars = count_chars(book_text)

  char_list = []

  for c in chars:
     if c.isalpha():
        char_list.append({"char": c, "num": chars[c]})

  char_list.sort(reverse=True, key=sort_on)

  char_list_str = ''

  for char in char_list:
     char_list_str += f"The '{char['char']}' character was found {char['num']} times\n  "

  return f"""
  --- Begin report of books/frankenstein.txt ---
  {words} words found in the document

  {char_list_str}
  --- End Report ---
  """

def main():
  f = open("./books/frankenstein.txt")
  book_text = f.read()

  print(gen_report(book_text))

if __name__ == "__main__":
    main()