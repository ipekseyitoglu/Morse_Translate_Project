

# Define the Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' ', '.': '.-.-.-', ',': '--..--', '?':'..--..', '!': '-.-.--', 
    ':': '---...', ';': '-.-.-.', '+': '.-.-.', '-': '-....-', '=' : '-...-',
    '/':'-..-.', '"': '.-..-.', "'": '.----.', '(': '-.--.', ')': '-.--.-',
    '&' : '.-...', '$': '...-..-', '@': '.--.-.'
    }

# Function to encode text to Morse code

def text_to_morse(text):
    text = text.upper()
    morse_code = ''
    for char in text:
        if char in morse_code_dict:
            if char == ' ' :
                morse_code += morse_code_dict[char]
            else : 
                morse_code += morse_code_dict[char]+ ' '
    return morse_code

# Function to decode Morse code to text

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for char, morse in morse_code_dict.items():
            if code == morse:
                text += char
                # break 
        if code == '':
            text += ' '
    return text



# Example usage for encoding

text_to_encode = "Hello World"
morse_code_result = text_to_morse(text_to_encode)
print(f"Text: {text_to_encode}")
print(f"Morse Code: {morse_code_result}")

# Example usage for decoding

morse_to_decode = " .... . .-.. .-.. ---  .-- --- .-. .-.. -.."
decoded_text_result = morse_to_text(morse_to_decode)
print(f"Morse Code: {morse_to_decode}")
print(f"Decoded Text: {decoded_text_result}")