"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    array = []
    #chek: odd or even amount of chars
    #even
    if len(s)%2 == 0:
        #chek: amount of chars = 0 ?
        if len(s) == 0:
            return array
        else:
            for i in range(0, len(s), 2):
                array.append(s[i:i+2])
    #odd
    else:
        for i in range(0, len(s), 2):
            array.append(s[i:i+2])
        #adding '_' to the last one
        array[-1] +='_'
    return array