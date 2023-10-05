"""direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))"""

import string
from unidecode import unidecode


def ceasar_cypher_encode(string_to_encode, cypher_shift):
    """Function receives a string to be encoded acording to Ceasar Cypher method ,
    and a integer as the cypher's shift. Returns the encoded string. Needs the string library,
    and unidecode package because Romans didnt have accentuation
    """

    alfabet = string.ascii_lowercase
    string_to_encode = unidecode(string_to_encode).lower()
    # string_to_encode = string_to_encode.lower()

    encoded = ""

    for index, value in enumerate(string_to_encode):
        position_in_alfabet_string = alfabet.find(string_to_encode[index])

        encoded_index = position_in_alfabet_string + cypher_shift

        if (position_in_alfabet_string + cypher_shift) >= len(alfabet):
            encoded_index = encoded_index - len(alfabet)

        if position_in_alfabet_string == -1:
            encoded = encoded + " "

        else:
            encoded = encoded + alfabet[encoded_index]

    return encoded


print(ceasar_cypher_encode("Douglas é um grande amigo", 10))
