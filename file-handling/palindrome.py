with open('words.txt', 'r') as file:
    for words in file:
        words = words.strip()
        if(words == words[::-1]):
            with open('palindrome.txt', 'w') as pal:
                pal.writelines(words)