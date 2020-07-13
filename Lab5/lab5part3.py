

def reverse(s):
    return s[::-1]

def palindrome(s):
    rev = reverse(s)
    if (s==rev):
        return True
    return False

s = "madam"
ans = palindrome(s)

if ans == 1:
    print("Input is a palindrome")
else:
    print("Input is not a palindrome")