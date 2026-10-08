def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch

        charCount = charCount + 1

    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]

    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

def encryptMessage():
    msg = input("Enter a message to encrypt: ")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is: ", cipherText)

def letterToIndex(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    idx = alphabet.find(letter)
    if idx == -1:
        print("Error: Letter not in the alphabet.", letter)

    return idx

def indexToLetter(idx):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    letter = ''
    if idx > 25:
        print("Error: ", idx, " is too large.")
    elif idx < 0:
        print("Error: ", idx, " is less than 0.")
    else:
        letter = alphabet[idx]

    return letter

def vigenereIndex(keyLetter, plainTextLetter):
    keyIndex = letterToIndex(keyLetter)
    ptIndex = letterToIndex(plainTextLetter)
    newIdx = (ptIndex +  keyIndex) % 26

    return indexToLetter(newIdx)

def encryptVigenere(key, plainText):
    cipherText = ""
    keyLen = len(key)
    for i in range(len(plainText)):
        ch = plainText[i]
        if ch == '':
            cipherText = cipherText + ch
        else:
            cipherText = cipherText + vigenereIndex(key[i % keyLen], ch)

    return cipherText

#print(scramble2Encrypt("Hello World!"))
#print(scramble2Decrypt(scramble2Encrypt("Hello World!")))

#encryptMessage()

print("Our encrypted value is: ", vigenereIndex('d', 'y'), "This is another output.", sep="I am the sep value :-)")

print(encryptVigenere("gmnzopabxycdefqrstuhijklvw ", "hello world"))
