## Challenge 1: Reverse a String 
## Write a function to reverse a given string without using built-in functions like reversed().
## Expected function: my_reversed(word: str -> str].
## Hint: Explore how negative indexing works in Python

def my_reversed(word: str) -> str:
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1): ## Moves from the last index to the first
        reversed_word += word[i] ## Append each character in reverse order
    return reversed_word

## Challenge 2: Count vowels and consonants
## Write a function that counts the number of vowels and consonants in a string (ignorning non alphabetic characters)
## Expected function: how_many(word: str -> tuple(vowels: int, consonants: int))

def how_many(word: str) -> tuple:
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isalpha(): ## Checks if the character is alphabetical or not
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

## Challenge 3: Palindrome Check
## Write a function to check if a string is a palindrome ignoring non alpha-numeric characters (Return True if it is, False if it isn't)
## Expected function: palindrome(possible_palindrome: str -> bool)

def palindrome(possible_palindrome: str) -> bool:
    ## Filter non-alphanumeric characters and convert lowercase
    filtered_string = ''.join(char.lower() for char in possible_palindrome if char.isalnum())
    
    ## Check if the filtered string is a palindrome
    return filtered_string == filtered_string[::-1] ## [::-1] its a slice to invert a sequence. In this case it is showing running backwards the string

## Challenge 4: Format Phone Number
## i. Separate the extension from the phone number, eliminating any leading or trailing spaces.
## ii. According to a parameter country, add the country phone code to the phone number. Note that numbers must not begin with zero before applying the country code. Assume the only countries possible are "Colombia" and "Brazil".
## iii. Arrange the resulting number as follows: (+XXX) XXXX XXXXXX
## Expected fuinction: format_phone(phone_number: str, country: str) -> tuple(phone: str, ext: str)]
## Example: If the country is "Colombia", and the phone number is "0-080-456-730 ext 88 ", then, the resulting tuple should be: ("(+57) 8045 6730", "ext 88").

def format_phone(phone_number: str, country: str) -> tuple:
    country_codes = {
        "Brazil": "+55",
        "Colombia": "+57"
    }
    
    ## Separates the ext number
    parts = phone_number.split("ext")
    phone_part = parts[0].strip()
    ext_part = f"ext {parts[1].strip()}" if len(parts) > 1 else "" ## Check if its an extension
    
    ## Removes leading zeros and non-digit chars
    digits_only = ''.join(char for char in phone_part if char.isdigit())
    if digits_only.startswith('0'):
        digits_only = digits_only.lstrip('0')
    
    ## Adds the country code
    if country in country_codes:
        country_codes = country_codes[country]
    else:
        raise ValueError("Invalid country")
    
    ## Formats the number
    formatted_phone = f"({country_codes}) {digits_only[:4]} {digits_only[:4]}"
    
    return f"({formatted_phone})", ext_part

print(format_phone("0-080-456-730 ext 88 ", "Colombia"))