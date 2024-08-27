# check if a string is a palindrome or not

def palindrome(s):
    try:
        if (s.lower() == s[::-1].lower()):
            print("is a palindrome")
        else:
            print("is not a palindrome")
    except:
        print("please enter a word")


palindrome("Yey")
