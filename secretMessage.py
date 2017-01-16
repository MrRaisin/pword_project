
def cypher(message, encrypt = True, shift_key = 3):
    decrypted_text = ''
    encrypted_text = ''
    # check if we are encrypting or decrypting
    if encrypt:
        for i in range(0, len(message)):
            encrypted_text += chr(ord(message[i]) - shift_key)
        #return
        return encrypted_text
    else:
        for i in range(0, len(message)):
            decrypted_text += chr(ord(message[i]) + shift_key)
            #return
        return decrypted_text
    

def main():
    plaintext = 'hello world'
    encryptedtext = cypher(plaintext, True, 2)
    print('encrypted:',encryptedtext)
    decryptedtext = cypher(encryptedtext,False, 2)
    print('decrypted:',decryptedtext)

if __name__ == "__main__":
    # execute only if run as a script
    main()


