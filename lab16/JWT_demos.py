# ----------------------------- Structure of JWT ----------------------------- #
# import base64

# # jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'

# def add_padding(byte_string):
#     pad_count = len(byte_string)%4
#     byte_string += (b'=' * pad_count)
#     return byte_string

# header = b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
# decoded_header = base64.decodebytes(header)
# print(decoded_header)

# payload = b'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ'
# decoded_payload = base64.decodebytes(add_padding(payload))
# print(decoded_payload)


# signature = b'SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
# decoded_signature = base64.decodebytes(add_padding(signature))
# print(decoded_signature)

# ------------------------------- Generate JWT ------------------------------- #
import jwt

encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
print(encoded_jwt)

decoded_jwt = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
print(decoded_jwt)