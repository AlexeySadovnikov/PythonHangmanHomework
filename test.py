import unittest

from hangman.Hangman import Hangman


class TestHangman(unittest.TestCase):
    def test_init(self):
        play = Hangman(word="bmw")
        self.assertEqual(play.word, "bmw")
        self.assertEqual(play.total_word, "***")
        self.assertEqual(play.num_try, 0)

    def test_init2(self):
        play = Hangman(word="toyota", all_try=4)
        self.assertEqual(play.word, "toyota")
        self.assertNotEqual(play.word, "t")
        self.assertEqual(play.total_word, "******")
        self.assertEqual(play.num_try, 0)
        self.assertEqual(play.all_try, 4)
        self.assertNotEqual(play.all_try, 2)

    def test_word(self):
        play = Hangman(word="bmw")
        self.assertEqual(play.word, "bmw")
        self.assertNotEqual(play.word, "bma")
        self.assertNotEqual(play.word, "b")

    def test_total_word(self):
        play = Hangman(word="bmw", all_try=5)
        play.guess("w")
        self.assertEqual(play.total_word, "**w")
        self.assertNotEqual(play.total_word, "b")
        self.assertNotEqual(play.total_word, "m")

    def test_total_word2(self):
        play = Hangman(word="audi", all_try=3)
        play.guess("9")
        self.assertNotEqual(play.total_word, "a")
        self.assertNotEqual(play.total_word, "u")
        self.assertNotEqual(play.total_word, "d")
        self.assertNotEqual(play.total_word, "i")

    def test_all_try(self):
        play = Hangman(word="bmw", all_try=6)
        self.assertEqual(play.all_try, 6)
        self.assertNotEqual(play.all_try, 3)

    def test_num_try(self):
        play = Hangman(word="bmw", all_try=5)
        play.guess("z")
        play.guess("b")
        play.guess("a")
        self.assertEqual(play.num_try, 2)

    def test_is_final(self):
        play = Hangman(word="bmw")
        play.guess("b")
        play.guess("m")
        self.assertFalse(play.is_final())
        play.guess("w")
        self.assertTrue(play.is_final())

    def test_is_final2(self):
        play = Hangman(word="audi", all_try=10)
        self.assertEqual(play.num_try, 0)
        play.guess("9")
        self.assertEqual(play.num_try, 1)
        self.assertFalse(play.is_final())
        play.guess("r")
        self.assertFalse(play.is_final())
        self.assertEqual(play.num_try, 2)
        play.guess("w")
        self.assertFalse(play.is_final())
        self.assertEqual(play.num_try, 3)
        play.guess("a")
        self.assertFalse(play.is_final())
        self.assertEqual(play.num_try, 3)
        play.guess("b")
        self.assertFalse(play.is_final())
        self.assertEqual(play.num_try, 4)
        play.guess("d")
        self.assertFalse(play.is_final())
        self.assertEqual(play.num_try, 4)
        play.guess("u")
        self.assertFalse(play.is_final())
        self.assertEqual(play.num_try, 4)
        play.guess("i")
        self.assertEqual(play.num_try, 4)
        self.assertTrue(play.is_final())

    def test_is_win(self):
        play = Hangman(word="bmw")
        play.guess("b")
        self.assertFalse(play.is_win())
        play.guess("m")
        self.assertFalse(play.is_win())
        play.guess("9")
        self.assertFalse(play.is_win())
        play.guess("au")
        self.assertFalse(play.is_win())
        play.guess("w")
        self.assertTrue(play.is_win())

    def test_guess(self):
        play = Hangman(word="bmw", all_try=5)
        self.assertFalse(play.guess("a"))
        self.assertFalse(play.guess("9"))
        self.assertTrue(play.guess("b"))

    def test_guess2(self):
        play = Hangman(word="mercedes", all_try=4)
        self.assertFalse(play.guess("z"))
        self.assertTrue(play.guess("e"))
        self.assertFalse(play.guess(""))
