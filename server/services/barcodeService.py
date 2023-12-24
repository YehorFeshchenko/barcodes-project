from barcode import Code39
from barcode.writer import ImageWriter
from barcode.errors import BarcodeError

import cv2
from pyzbar import pyzbar


class BarcodeService:

    def __init__(self):
        pass

    @staticmethod
    def decode(img_name):
        print('Image name: ' + img_name)
        try:
            if img_name is not None:
                image = cv2.imread('./static/images/' + img_name)
                decoded_objects = pyzbar.decode(image)
                for obj in decoded_objects:
                    decoded_data = obj.data.decode("utf-8")
                    print("Barcode Data:", decoded_data)
                    return decoded_data
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
            barcode_image = Code39(data, writer=ImageWriter(format='png'), add_checksum=False)
            barcode_image.save('./static/images/' + data, options={"module_width": 0.4, "module_height": 20})
        except Exception as e:
            print(f'Error encoding: {e}')
