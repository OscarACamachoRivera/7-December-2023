with open(r"c:/Users/Student/Downloads/final/final/notes.txt", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if 'alumno A' in line:
            print('string found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
            # don't look for next lines
            break
        