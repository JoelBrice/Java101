
file = open('text.txt') # Open for reading only (r)

print(file)

#f = open('text.txt', w) # Open to write
#f = open('text.txt', wr) #open to read and write


with open('text.txt', encoding="utf-8") as f:
    f.read()
    f.close()


