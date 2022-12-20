def swap_case(s):
    newString = ""
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            newString += chr(ord(char) + 32)
        elif ord(char) >= 97 and ord(char) <= 122:
            newString += chr(ord(char) - 32)
        else:
            newString += char
    return newString

if __name__ == '__main__':
