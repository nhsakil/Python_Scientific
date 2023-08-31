def is_palindrome(s):
    s = s.lower()  # Convert to lowercase to ignore case
    s = ''.join(filter(str.isalnum, s))  # Remove non-alphanumeric characters
    return s == s[::-1]  # Compare the string with its reverse


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")