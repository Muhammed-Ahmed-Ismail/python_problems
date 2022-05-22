def remove_vowels(str):
    return str.replace('o', '').replace('i', '').replace('e', '').replace('u', '').replace('a', '')


input_str = input("Enter a string to remove vowels from it: ")

print(remove_vowels(input_str))
