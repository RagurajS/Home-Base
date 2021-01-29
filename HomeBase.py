print("\nThis tool will Encrypt & Decrypt given gibberish with all Base encoding family. (base16, base32, base64, base85 & as well as by bytes... \n\t *** Created by Ragu ***, tool in beta version.\n\n")
import base64

choice = input("If you want to decrypt enter 'D' or if you wanna encrypt enter 'E': ")
if (choice == 'D'):
    decode = input("Enter something to decode by base family: ")
    # try:
    #     print("\nAs bytes Encoded: ", base64.decodebytes(decode))
    # except:
    #     print("\nIt's not an bytes encoded, trying to decode with base16 algorithm...")
    try:
        print("Base16 Decoded: ", base64.b16decode(decode))
    except:
        print("It's not an base16 encoded, trying to decode with base32 algorithm...")
    try:
        print("Base32 Decoded: ", base64.b32decode(decode))
    except:
        print("It's not an base32 encoded, trying to decode with base64 algorithm...")
    try:
        print("Base64 Decoded: ", base64.b64decode(decode).strip())
    except:
        print("It's not an base64 encoded, trying to decode with base85 algorithm...")
    try:
        print("Base85 Decoded: ", base64.b85decode(decode))
    except:
        print("It's not an base85 encoded, it's not base85 algorithm...")


elif (choice =='E'):
    encode = input("Enter something to encode by base family: ")
    # try:
    #     encode1 = encode.encode('ascii')
    #     encode2 = base64.encodebytes(encode1)
    #     encode3 = encode2.decode('ascii')
    #     print("\nEncoded by Bytes:  ",encode3, end='')
    # except:
    #     print("\nSo sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b16encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base16: ",encode3)
    except:
        print("So sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b32encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base32: ",encode3)
    except:
        print("So sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b64encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base64: ",encode3)
    except:
        print("So sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b85encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base85: ",encode3)
    except:
        print("So sorry, Something went wrong..")

else:
    print("Wrong selected you've made, Give 1 or 2 as return!")
