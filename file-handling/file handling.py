with open('words.txt', 'r') as file:
    for line in file:
        print(line)


lines= ('welcome', 'cow', 'manager')
with open('text.txt', 'w') as textfile:
    textfile.writelines(lines)