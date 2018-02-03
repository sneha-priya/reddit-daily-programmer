CODE = {'A': 'h', 'B': '-...', 'C': '-.-.',
        'D':'-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--',  'N': '-.',  'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
     	'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        
        }

def to_morse(msg):
    global CODE
    result = []
    for item in msg:
        result.append(CODE[item.upper()])
    morse = "|".join(result)
    return morse

def from_morse(morse):
    CODE_REVERSE = {value:key for key,value in CODE.items()}
    result = []
    string = morse.split("|")
    for item in string:
        result.append(CODE_REVERSE.get(item))
    decode = "".join(result)
    return decode
if __name__ == "__main__":
    msg = str(input("Enter a sentence or a word to encode it into morse code: "))
    morse_code = to_morse(msg)
    print("The encoded morse code is {} ".format(morse_code))
    decoded_morse = from_morse(morse_code)
    print("The decoded morse code is {}".format(decoded_morse))