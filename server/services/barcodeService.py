from barcode import Code39
from barcode.writer import ImageWriter
from barcode.errors import BarcodeError

import cv2
from pyzbar import pyzbar

# Mapping for non-standard characters in Code 39 Full ASCII
full_ascii_map = {
    ' ': '/A', '!': '/B', '"': '/C', '#': '/D', '$': '/E', '%': '/F', '&': '/G', '\'': '/H', '(': '/I', ')': '/J',
    '*': '/K', '+': '/L', ',': '/M', '-': '/N', '.': '/O', '/': '/P', '0': '0', '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', ':': '/Z', ';': '%F', '<': '%G', '=': '%H',
    '>': '%I', '?': '%J', '@': '%V', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G',
    'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q',
    'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z', '[': '%K',
    '\\': '%L', ']': '%M', '^': '%N', '_': '%O', '`': '%W', 'a': '+A', 'b': '+B', 'c': '+C', 'd': '+D',
    'e': '+E', 'f': '+F', 'g': '+G', 'h': '+H', 'i': '+I', 'j': '+J', 'k': '+K', 'l': '+L', 'm': '+M',
    'n': '+N', 'o': '+O', 'p': '+P', 'q': '+Q', 'r': '+R', 's': '+S', 't': '+T', 'u': '+U', 'v': '+V',
    'w': '+W', 'x': '+X', 'y': '+Y', 'z': '+Z', '{': '%P', '|': '%Q', '}': '%R', '~': '%S'
}


class BarcodeService:

    def __init__(self):
        pass

    @staticmethod
    def decode(img_path):
        try:
            if img_path is not None:
                image = cv2.imread(img_path)
                decoded_objects = pyzbar.decode(image)
                for obj in decoded_objects:
                    decoded_data = obj.data.decode("utf-8")
                    barcode_data = decode_full_ascii(decoded_data)
                    print("Barcode Data:", barcode_data)
                    return barcode_data
            else:
                print('Error: No image file')
                return
        except BarcodeError as err:
            print(f'Error decoding: {err}')
            return None

    @staticmethod
    def generate(data):
        try:
            print('Generating barcode for: ' + data)
            encoded_data = encode_full_ascii(data)
            barcode_image = Code39(encoded_data, writer=ImageWriter(format='png'))
            barcode_image.save('./images/' + data, options={"module_width": 0.4, "module_height": 20})
            print(barcode_image.name)
            return barcode_image.name
        except Exception as e:
            print(f'Error encoding: {e}')


def decode_full_ascii(encoded_string):
    # Reverse mapping for Full ASCII Code 39
    reverse_full_ascii_map = {v: k for k, v in full_ascii_map.items()}

    decoded_string = ''
    i = 0
    while i < len(encoded_string):
        if encoded_string[i] in reverse_full_ascii_map:
            # Single character mapping
            decoded_string += reverse_full_ascii_map[encoded_string[i]]
            i += 1
        elif i + 1 < len(encoded_string) and encoded_string[i:i + 2] in reverse_full_ascii_map:
            # Double character mapping
            decoded_string += reverse_full_ascii_map[encoded_string[i:i + 2]]
            i += 2
        else:
            # Character not found in mapping
            decoded_string += '?'
            i += 1

    return decoded_string


def encode_full_ascii(data):
    encoded_data = ''
    for char in data:
        if char in full_ascii_map:
            encoded_data += full_ascii_map[char]
        else:
            encoded_data += char
    return encoded_data
