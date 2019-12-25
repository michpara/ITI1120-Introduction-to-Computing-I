def is_palindrome_v2(word):
    '''(string)->boolean
    returns if word is palindrome (ignores white space)'''
    if len(word) < 2:
        return True
    if(not word[0].isalpha() or not word[1].isalpha()):
        if(word[0].isalpha()):
            return is_palindrome_v2(word[:-1])
        if(word[-1].isalpha()):
            return is_palindrome_v2(word[1:])
        else:
            return is_palindrome_v2(word[2:-2])
    if word[0].lower() != word[-1].lower():
        return False
    return is_palindrome_v2(word[1:-1])
    
