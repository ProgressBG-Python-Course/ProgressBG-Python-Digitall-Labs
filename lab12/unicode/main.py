# ------------------------------ ord() and chr() ----------------------------- #
# print( ord('Я') ) #1071(10) => 42F(16)

# # Ѧ => U+0466
# code_point_in_hex = '0x0466'
# print(code_point_in_hex)
# code_point_in_dec = int(code_point_in_hex, base=16)
# print(code_point_in_dec)

# print( chr(code_point_in_dec) )


# Unicode symbol in string:
# print("Ѣ")

# # Using the character name:
# print("\N{Cyrillic Capital Letter Yat}")

# # Using a 16-bit hex value code point:
# print("\u0462")

# # Using a 32-bit hex value code point:
# print("\U00000462")



# --------------------------------- encode() --------------------------------- #
# text = 'абв'
# text_bytes = text.encode(encoding='utf-8')
# print(text_bytes)

# print(len(text))
# print(len(text_bytes))

# text = 'абв'
# try:
#     text_bytes = text.encode(encoding='ascii') # UnicodeEncodeError
# except UnicodeEncodeError as e:
#     print(e)
#     exit(-1)
# except Exception as e:
#     print('Ups, something went wrong')

# print(text_bytes)

# --------------------------------- decode() --------------------------------- #
# byte_string =  b'\xd0\xb0\xd0\xb1\xd0\xb2'
# print(type(byte_string))

# string = byte_string.decode(encoding='cp1251')
# string = byte_string.decode(encoding='utf-8')

# print("String object:", string)
# print("Type: ",type(string) )
# print("String length:",len(string) )
# print("Byte_string length:",len(byte_string) )

# String object: абв
# Type:  <class 'str'>
# String length: 3
# Byte_string length: 6




# ------------------------------- bytes object ------------------------------- #
# byte_data = bytes([72, 101, 108, 108, 111])
# print("Bytes Object:", byte_data)

# string = byte_data.decode(encoding='utf-8')
# print(string)


# -------------------------- save file with encoding ------------------------- #
# string = "Петър плет плете"

# # open a file for writing in text mode, with encoding="cp1251" "
# with open("write_to_cp1251.txt", "w", encoding="cp1251") as fh:
#     fh.write(string)

# print('File saved')


# ---------------------------------- base64 ---------------------------------- #
# import base64

# # base64 needs binary data:
# data_bytes = 'яиуруи'.encode()

# # encoding binary data to Base64
# data_base64 = base64.b64encode(data_bytes)
# print(f'data_base64: {data_base64}')

# # decoding Base64-encoded data back to binary
# decoded_data_bytes = base64.b64decode(data_base64)
# print("Decoded:", decoded_data_bytes.decode())

# import json

# bytes = 'яиуруи'.encode()

# data = {
#     'user_name': bytes
# }

# string_json = json.dumps(data)
# print(string_json)

### Use - case
import json
import base64

def save_image_bytes_from_json(data_json):

    data = json.loads(data_json)
    image_base64 = data['image']

    # Decode Base64 data
    image_bytes = base64.b64decode(image_base64)

    # Save decoded image to a file
    with open(data['filename'], "wb") as img_file:
        img_file.write(image_bytes)

    print(f'{data["filename"]} saved!')

# JSON data containing image information
data_json = """
{
    "filename": "example_image.jpg",
    "type": "image/png",
    "image": "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAcElEQVR4nGI5y9PLAAOfJ3HB2VeWS8HZH7hmwNlMDCQC2mtgOb/hKJyzIy4Lzrbdpg5nV8Tcp6OTSNbAKMk+Dc7JUV0IZ7+PmwRn34zgpKOTSI8H2QUucE7q329wtv2hWDj7D6sCHZ1EsgZAAAAA//9eCxes6NHYOQAAAABJRU5ErkJggg==",
    "size": 152347,
    "url": "https://yulvil.github.io/gopherjs/02/"
}
"""

save_image_bytes_from_json(data_json)
