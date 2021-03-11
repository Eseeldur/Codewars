"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    a=text.split()
    for i in range(len(a)):
        if a[i]!='?'and a[i]!='!':
            a[i] = a[i][1:] + a[i][0] + 'ay'
    text = ' '.join(a)
    return text