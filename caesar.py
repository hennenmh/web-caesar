def encrypt(text, rot):
    new_text = ''
    for char in text:
        new_char = rotate_character(char, rot)
        new_text += new_char
    return new_text

def alphabet_position(letter):
        if (letter.isupper()):
            pos = ord(letter) - 65
        else:
            pos = ord(letter) - 97
        return pos

def rotate_character(char, rot):
        rot = int(rot)
        char_pos = alphabet_position(char)
        if (char.isupper()):
            new_char_pos = ((char_pos + rot) % 26) + 65
        elif (char.islower()):
            new_char_pos = ((char_pos + rot) % 26) + 97
        else:
            return char
        return chr(new_char_pos)
