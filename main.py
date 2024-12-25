def count_words(book):
   num = 0
   inArray = book.split()
   for word in inArray:
      num += 1
   
   #print(num)
   return num

def count_chars(book):
   dic = {}

   num = 0
   lowerCaseBook = book.lower()
   for c in lowerCaseBook:
      if (c not in dic and c in "pygcrlaoeuidhtnsqkjxbmwvz"):
         dic[c] = 1
      elif (c in "pygcrlaoeuidhtnsqkjxbmwvz"):
         dic[c] += 1
   
   listo = []

   for key in dic:
      listo.append({"name": key, "num": dic[key]})

   #print(listo)
   return listo

def sort_on(dict):
   return dict["num"]

def main():
   with open("books/frankenstein.txt") as f:
      file_contents = f.read()
      #print(file_contents)
      print("--- Begin report of books/frankenstein.txt ---")
      words = count_words(file_contents)
      print(f"{words} words found in the document")
      print()

      daList = count_chars(file_contents)
      daList.sort(reverse=True, key=sort_on)

      for item in daList:
         print(f"The '{item['name']}' character was found {item['num']} times")
      #print(daList)
      print("--- End report ---")
main()