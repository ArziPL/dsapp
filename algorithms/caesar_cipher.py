# O(n) - takes word and rearranges letters by key positions in
# alphabet. If character is lower/bigger then ASCII code of
# character then +26/-26 to get back into ASCII subset with letters

def ceasar_encryption(word, key):
    key = key % 26
    encrypted_word = []
    for i in word:
        character = chr(ord(i) + key)
        if character > "z":
            character = chr(ord(i) + key - 26)
        encrypted_word.append(character)
    return "".join(encrypted_word)


def ceasar_decryption(word, key):
    key = key % 26
    decrypted_word = []
    for i in word:
        character = chr(ord(i) - key)
        if character < "a":
            character = chr(ord(i) - key + 26)
        decrypted_word.append(character)
    return "".join(decrypted_word)


print(ceasar_encryption("pythoniscool", 5))  # should be "udymtsnxhttq"
print(ceasar_decryption("udymtsnxhttq", 5))  # should be "pythoniscool"
