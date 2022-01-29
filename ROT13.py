'''
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.
'''

# Solution 1 --------
def rot13(message):
    new_mes = ''
    dictionary = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q',
                  'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U',
                  'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y',
                  'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
                  'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
                  'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K',
                  'Y': 'L', 'Z': 'M', 'a': 'n', 'b': 'o',
                  'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
                  'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
                  'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a',
                  'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e',
                  's': 'f', 't': 'g', 'u': 'h', 'v': 'i',
                  'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
                  ' ': ' ', '.': '.', '!': '!', ')': ')',
                  ',': ',', '(': '(', ':': ':', '?': '?',
                  '-': '-', '_': '_', '"': '"', "'": "'",
                  '1': '1', '2': '2', '3': '3', '4': '4',
                  '5': '5', '6': '6', '7': '7', '8': '8',
                  '9': '9', '0': '0', '\n': '\n', '@': '@',
                  '[': '[', '`': '`', '{': '{', '}': '}',
                  '/': '/', '^': '^', '+' :'+', '\x0b': '\x0b',
                  '\r': '\r', '~': '~', '\\': '\\', '\t': '\t',
                    '*': '*', ';': ';', '>': '>', '|': '|', ']': ']', 
                 '[': '[', '\x0c': '\x0c', '=': '=', '#': '#',
                 '%': '%', '<': '<', '&': '&', '$': '$'}
    for dig in message:
        new_mes = new_mes + dictionary[dig]
    return new_mes
  
  
  # Solution 2 ---------
  def rot13(message):
    root13in = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    root13out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    root13map = dict(zip(root13in, root13out))
    
    new_mes = ''.join([root13map.get(s, s) for s in message])
    
    return new_mes
