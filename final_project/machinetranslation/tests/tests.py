import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french(self):
        # Test for null input
        self.assertNotEqual(english_to_french(0), 0)
        # Test for the translation of the world ‘Hello’ and ‘Bonjour’.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test for word translated or returned the input without translation
        self.assertNotEqual(english_to_french('Hello'), 'Hello')


class TestFrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        # Test for null input
        self.assertNotEqual(french_to_english(0), 0)
        # Test for the translation of the world ‘Hello’ and ‘Bonjour’.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Test for word translated or returned the input without translation
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')


unittest.main()
