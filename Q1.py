def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
s= input("Enter a word or phrase: ").lower()
if is_palindrome(s):
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")
