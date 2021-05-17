def solution(x):
    # Your code here
    import string
    plain = string.ascii_lowercase
    coded = string.ascii_lowercase[::-1]
    decoded_msg = ''
    
    decoded_msg = [letter if letter not in coded else plain[coded.index(letter)] for letter in x]
    
    decoded_msg = ''.join(decoded_msg)
    
    return decoded_msg
