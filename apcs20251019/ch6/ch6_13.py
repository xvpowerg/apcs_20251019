find1 = open("Poem.txt",encoding="cp950")
line = find1.readlines()
print(line)

find1 = open("PoemUTF8.txt",encoding="utf-8")
line = find1.readlines()
print(line)
