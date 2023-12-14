# string to search in file
word = 'alumno D'
with open(r'c:/Users/Student/Downloads/final/final/notes.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Record completo:', line)
            #--------------------------
            # Crear lista
            x = []
            x.append(line)           
            print(x) 
            x=line.split(",")
            print(x)
            suma=0
            suma=(float(x[1]) + float(x[2]) +float(x[3]))
            print((x[1]))
            print((x[2]))
            print(suma)
          
            
           
            
            
            
            