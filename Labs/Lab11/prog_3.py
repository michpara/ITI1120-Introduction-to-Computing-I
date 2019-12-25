def is_palindrome(word):
    '''(string)->boolean
    returns if word is a palindrome'''
    if len(word) < 2:
        return True
    if word[0].lower() != word[-1].lower():
        return False
    return is_palindrome(word[1:-1])
    
