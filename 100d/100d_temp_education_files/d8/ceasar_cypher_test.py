import unittest
import ceasar_cypher_functions

# TODO: Added colors to tests

class CaesarCipherTestCase(unittest.TestCase):
    def test_encrypt(self):
        plaintext = "Hello, World!"
        encrypted = ceasar_cypher_functions.ceasar_cypher_encode(plaintext, 3)
        self.assertEqual(encrypted, "Khoor, Zruog!")

    def test_decrypt(self):
        ciphertext = "Khoor, Zruog!"
        decrypted = ceasar_cypher_functions.ceasar_cypher_decode(ciphertext, 3)
        self.assertEqual(decrypted, "Hello, World!")

if __name__ == "__main__":
    unittest.main()