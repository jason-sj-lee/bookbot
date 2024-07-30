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

def main():
  f = open("./books/frankenstein.txt")
  book_text = f.read()

  print(count_chars(book_text))

if __name__ == "__main__":
    main()