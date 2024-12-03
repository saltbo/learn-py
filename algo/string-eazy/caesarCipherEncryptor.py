def caesarCipherEncryptor(string, key):
    # Write your code here.

    newCode = 0
    newChars = []
    for s in string:
        newCode = ord(s) + key % 26
        print(newCode)

        if newCode > 122:
            newCode = 96 + newCode

        newChars.append(chr(newCode))
    return "".join(newChars)        

print(caesarCipherEncryptor("xyz", 3))