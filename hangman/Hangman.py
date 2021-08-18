import random
from typing import Set
from string import ascii_lowercase


dictionary = ["mercedes", "bmw", "audi", "volkswagen", "toyota"]


class Hangman:
    def __init__(self, word: str = "mercedes", all_try: int = 5) -> None:
        self.__word = word.lower()
        self.__num_try = 0
        self.__maxnum_try = all_try
        self.__letter_guess: Set[str] = set()

    @property
    def word(self) -> str:
        return self.__word

    @property
    def total_word(self) -> str:
        return "".join(
            letter if letter in self.__letter_guess else
            "*" for letter in self.word
        )

    @property
    def num_try(self) -> int:
        return self.__num_try

    @property
    def all_try(self) -> int:
        return self.__maxnum_try

    def is_final(self) -> bool:
        return self.is_win() or self.__num_try >= self.__maxnum_try

    def is_win(self) -> bool:
        return self.word == self.total_word

    def guess(self, letter: str) -> bool:
        if len(letter):
            if letter not in ascii_lowercase:
                self.__num_try += 1
                return False
            if letter in self.word:
                self.__letter_guess.add(letter)
                return True
            if letter not in self.word:
                self.__num_try += 1
                return False
        return False


def play_hangman():
    play = Hangman(word=random.choice(dictionary))
    print("Guess a letter (The word is popular brand of car) :")
    while not play.is_final():
        enter = input("Enter a letter\n").lower()
        if play.guess(enter):
            print("Hit!\n")
            print("GuessingWord: " + play.total_word)
        else:
            print(
                "Missed, mistake "
                + str(play.num_try)
                + " out of "
                + str(play.all_try)
            )
    if play.is_win():
        print("You Win!")
    else:
        print("You Lost!")


if __name__ == "__main__":
    play_hangman()
