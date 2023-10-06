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


def ceasar_cypher_decode(string_to_decode, cypher_shift):
    """Function receives an encoded string acording to Ceasar Cypher method ,
    and a integer as the cypher's shift. Returns the decoded string. Needs the string library,
    """

    alfabet = string.ascii_lowercase

    decoded = ""
    for index, value in enumerate(string_to_decode):
        position_in_alfabet_string = alfabet.find(string_to_decode[index])

        decoded_index = position_in_alfabet_string - cypher_shift

        if (position_in_alfabet_string + cypher_shift) < 0:
            decoded_index = decoded_index + len(alfabet)

        if position_in_alfabet_string == -1:
            decoded = decoded + " "
        else:
            decoded = decoded + alfabet[decoded_index]

    return decoded
