# string to search in file
word = input("Nombre del archivo a buscar: ")
with open(r'c:/Users/Student/Downloads/final/final/dir.txt', 'r') as fp:
  # read all lines in a list
     lines = fp.readlines() 
     for line in lines:
   # not equal to
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)
         