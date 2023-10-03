def is_palindrome(input_str):

    input_str = input_str.lower().replace(' ', '')

    
    return input_str == input_str[::-1]

print(is_palindrome("Wow"))  
print(is_palindrome("hello"))  

